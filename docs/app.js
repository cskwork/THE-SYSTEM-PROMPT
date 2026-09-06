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
