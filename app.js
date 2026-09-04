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
