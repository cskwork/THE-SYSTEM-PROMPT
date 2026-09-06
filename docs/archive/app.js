(function () {
  var TEXT = window.COPY_MSG || { 'agents-md': 'AGENTS.md copied', 'install-block': 'Install block copied' };
  function announce(btn, msg) {
    var node = btn.parentElement, el = null;
    while (node && !el) { el = node.querySelector('.status'); node = node.parentElement; }
    if (!el) return;
    el.textContent = msg;
    clearTimeout(el._t);
    el._t = setTimeout(function () { el.textContent = ''; }, 2600);
  }
  function legacyCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.cssText = 'position:fixed;top:0;left:0;opacity:0;pointer-events:none';
    document.body.appendChild(ta);
    ta.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
    document.body.removeChild(ta);
    return ok;
  }
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('[data-copy]');
    if (!btn) return;
    var src = document.getElementById(btn.getAttribute('data-copy'));
    if (!src) return;
    var text = src.textContent;
    var done = function () { announce(btn, TEXT[src.id] || 'Copied'); };
    var failed = function () { announce(btn, 'Copy failed — select the text manually'); };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done, function () { legacyCopy(text) ? done() : failed(); });
    } else {
      legacyCopy(text) ? done() : failed();
    }
  });
})();

(function () {
  var loop = document.querySelector('.loop');
  if (!loop) return;
  if (!('IntersectionObserver' in window) ||
      window.matchMedia('(prefers-reduced-motion: reduce)').matches) { loop.classList.add('in'); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { loop.classList.add('in'); io.disconnect(); } });
  }, { rootMargin: '0px 0px -18% 0px' });
  io.observe(loop);
})();

(function () {
  var loop = document.querySelector('.loop');
  var T = window.WALK;
  if (!loop || !T || !('open' in document.createElement('details'))) return;
  var GATE = 4, steps = [].slice.call(loop.querySelectorAll('.step'));
  var prog = document.querySelector('.prog'), reset = document.querySelector('.reset');
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var approved = false;

  steps.forEach(function (s) { if (+s.dataset.step > GATE) s.classList.add('locked'); });

  function details(s) { return s.querySelector('.xd'); }
  function stepOf(el) { return el.closest('.step'); }
  function setCurrent(s) {
    steps.forEach(function (x) { x.classList.toggle('current', x === s); });
    if (!s) { prog.innerHTML = ''; return; }
    var n = +s.dataset.step, name = s.dataset.name;
    var line = T.prog.replace('{n}', n).replace('{name}', name), note = '';
    if (approved) note = '<span>' + T.approved + '</span>';
    else if (n === GATE) note = '<span class="wait">' + (s.classList.contains('hint') ? T.hint : T.waiting) + '</span>';
    prog.innerHTML = '<b>' + line + '</b>' + note;
  }
  function openStep(s, scroll) {
    var d = details(s);
    if (!d.open) d.open = true;
    setCurrent(s);
    if (scroll) s.scrollIntoView({ block: 'nearest', behavior: reduced ? 'auto' : 'smooth' });
  }
  // exclusive accordion for browsers without <details name>
  loop.addEventListener('toggle', function (e) {
    var d = e.target; if (!d.classList.contains('xd')) return;
    if (d.open) {
      loop.querySelectorAll('.xd[open]').forEach(function (o) { if (o !== d) o.open = false; });
      setCurrent(stepOf(d));
    } else if (stepOf(d).classList.contains('current')) setCurrent(null);
  }, true);
  // locked steps route the reader to the gate
  loop.addEventListener('click', function (e) {
    var sum = e.target.closest('summary'); if (!sum) return;
    var d = sum.parentElement, s = stepOf(d);
    if (d.classList.contains('locked') && !approved) {
      e.preventDefault();
      var gate = steps[GATE - 1];
      openStep(gate, true);
      gate.classList.add('hint');
      setCurrent(gate);
      setTimeout(function () { gate.querySelector('.approve').focus({ preventScroll: true }); }, 60);
    }
  });
  loop.addEventListener('click', function (e) {
    var b = e.target.closest('.approve'); if (!b) return;
    approved = true;
    loop.classList.add('approved');
    steps[GATE - 1].classList.remove('hint');
    steps.forEach(function (s) {
      if (+s.dataset.step > GATE) {
        s.classList.remove('locked');
        var d = details(s); d.classList.remove('locked'); d.removeAttribute('aria-disabled');
        d.querySelector('summary').lastChild.textContent = T.see;
      }
    });
    b.disabled = true;
    reset.hidden = false;
    prog.innerHTML = '<b>' + T.approved + '</b>';
    var rest = steps.slice(GATE), i = 0;
    (function next() {
      if (i >= rest.length) return;
      openStep(rest[i], true); i++;
      if (reduced) { if (i < rest.length) next(); }
      else setTimeout(next, 1400);
    })();
  });
  reset.addEventListener('click', function () {
    approved = false;
    loop.classList.remove('approved');
    loop.querySelectorAll('.xd[open]').forEach(function (o) { o.open = false; });
    steps.forEach(function (s) {
      s.classList.remove('hint', 'current');
      if (+s.dataset.step > GATE) {
        s.classList.add('locked');
        var d = details(s); d.classList.add('locked'); d.setAttribute('aria-disabled', 'true');
        d.querySelector('summary').lastChild.textContent = T.locked || d.querySelector('summary').lastChild.textContent;
      }
    });
    loop.querySelector('.approve').disabled = false;
    reset.hidden = true;
    setCurrent(null);
    steps[0].querySelector('summary').focus();
  });
  // arrow keys walk the summaries; Home/End jump
  loop.addEventListener('keydown', function (e) {
    var sum = e.target.closest('summary'); if (!sum) return;
    var sums = [].slice.call(loop.querySelectorAll('summary')), i = sums.indexOf(sum), to = null;
    if (e.key === 'ArrowDown' || e.key === 'j') to = sums[i + 1];
    else if (e.key === 'ArrowUp' || e.key === 'k') to = sums[i - 1];
    else if (e.key === 'Home') to = sums[0];
    else if (e.key === 'End') to = sums[sums.length - 1];
    if (to) { e.preventDefault(); to.focus(); }
  });
  window.WALK.locked = T.locked;
})();

(function () {
  // theme: explicit choice wins, system preference otherwise
  var btn = document.querySelector('.theme'); if (!btn) return;
  var labels = btn.dataset.labels.split('|'), root = document.documentElement;
  function effective() { return root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'); }
  function paint() { btn.textContent = effective() === 'dark' ? labels[1] : labels[0]; root.style.colorScheme = effective(); }
  try { var saved = localStorage.getItem('theme'); if (saved) root.dataset.theme = saved; } catch (e) {}
  btn.hidden = false; paint();
  btn.addEventListener('click', function () {
    root.dataset.theme = effective() === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('theme', root.dataset.theme); } catch (e) {}
    paint();
  });
})();

(function () {
  // deep links: #step-3 opens the step; opening a step writes the hash
  var loop = document.querySelector('.loop'); if (!loop) return;
  function fromHash() {
    var m = /^#step-(\d)$/.exec(location.hash); if (!m) return;
    var li = document.getElementById('step-' + m[1]); if (!li) return;
    var d = li.querySelector('.xd');
    if (d.classList.contains('locked')) { li = document.getElementById('step-4'); d = li.querySelector('.xd'); }
    d.open = true;
    setTimeout(function () { li.scrollIntoView({ block: 'start' }); window.scrollBy(0, -24); }, 30);
  }
  loop.addEventListener('toggle', function (e) {
    var d = e.target; if (!d.classList.contains('xd') || !d.open) return;
    var id = d.closest('.step').id;
    if (history.replaceState) history.replaceState(null, '', '#' + id);
  }, true);
  window.addEventListener('hashchange', fromHash);
  fromHash();
})();

(function () {
  // install configurator: the static block is the no-JS baseline and the default output
  var form = document.querySelector('.cfg'), out = document.querySelector('#install-block code');
  var vwrap = document.querySelector('.verify'), vout = document.querySelector('#verify-block code');
  var C = window.CFG; if (!form || !out || !C) return;
  var RAW = 'https://raw.githubusercontent.com/cskwork/THE-SYSTEM-PROMPT/main/AGENTS.md';
  var P = { claude: ['~/.claude/CLAUDE.md', '$HOME\\.claude\\CLAUDE.md'],
            codex: ['~/.codex/AGENTS.md', '$HOME\\.codex\\AGENTS.md'],
            gemini: ['~/.gemini/GEMINI.md', '$HOME\\.gemini\\GEMINI.md'],
            opencode: ['~/.config/opencode/AGENTS.md', '$HOME\\.config\\opencode\\AGENTS.md'],
            pi: ['~/.pi/agent/AGENTS.md', '$HOME\\.pi\\agent\\AGENTS.md'],
            repo: ['/path/to/your/repo/AGENTS.md', 'C:\\path\\to\\your\\repo\\AGENTS.md'] };
  function esc(t) { return t.replace(/&/g, '&amp;').replace(/</g, '&lt;'); }
  function render() {
    var agents = [].map.call(form.querySelectorAll('input[name=agent]:checked'), function (i) { return i.value; });
    var win = form.querySelector('input[name=shell]:checked').value === 'win';
    var lines = [], check = [];
    if (win) {
      lines.push('New-Item -ItemType Directory -Force "$HOME\\.agents" | Out-Null');
      lines.push('Invoke-WebRequest <span class="u">' + RAW + '</span> -OutFile "$HOME\\.agents\\AGENTS.md"', '', '<span class="c">' + esc(C.wincopy) + '</span>');
      agents.forEach(function (a) {
        lines.push('Copy-Item "$HOME\\.agents\\AGENTS.md" "' + P[a][1] + '" -Force' + (a === 'gemini' ? '   <span class="c">' + esc(C.gemini) + '</span>' : ''));
        check.push('Get-FileHash "' + P[a][1] + '" | Select-Object -ExpandProperty Hash');
      });
      check.unshift('Get-FileHash "$HOME\\.agents\\AGENTS.md" | Select-Object -ExpandProperty Hash   <span class="c"># every line below must match this one</span>');
    } else {
      lines.push('mkdir -p ~/.agents', 'curl -fsSL <span class="u">' + RAW + '</span> \\', '  -o ~/.agents/AGENTS.md', '');
      agents.forEach(function (a) {
        var pad = a === 'gemini' ? '            <span class="c">' + esc(C.gemini) + '</span>' : '';
        lines.push('ln -sfn ~/.agents/AGENTS.md ' + P[a][0] + pad);
        check.push('readlink ' + P[a][0]);
      });
      check.push('<span class="c"># each line prints ' + esc('/Users/you/.agents/AGENTS.md') + ' or the equivalent home path</span>');
    }
    out.innerHTML = lines.join('\n');
    vout.innerHTML = check.join('\n');
    vwrap.hidden = agents.length === 0;
  }
  form.hidden = false;
  form.addEventListener('change', render);
  render();
})();
