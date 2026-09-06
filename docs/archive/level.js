(function () {
  var world = document.getElementById('world'), stations = [].slice.call(world.querySelectorAll('.station'));
  var where = document.querySelector('.where'), dots = [].slice.call(document.querySelectorAll('.rail button'));
  var prev = document.querySelector('.nav.prev'), next = document.querySelector('.nav.next');
  var flatBtn = document.querySelector('.flat-toggle'), body = document.body;
  var GATE = 4, LAST = stations.length - 1, cur = 0, approved = false, busy = false;
  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

  function name(i) { return stations[i].querySelector('h2').textContent; }
  function paint() {
    stations.forEach(function (s, i) {
      var d = i - cur;
      s.dataset.dist = Math.abs(d);
      s.classList.toggle('passed', d < 0);
      s.setAttribute('aria-hidden', i === cur ? 'false' : 'true');
    });
    world.style.setProperty('--cur', cur);
    dots.forEach(function (b, i) { if (i === cur) b.setAttribute('aria-current', 'true'); else b.removeAttribute('aria-current'); });
    prev.disabled = cur === 0;
    next.disabled = cur === LAST;
    var label = cur === 0 ? 'Before the loop' : cur === LAST ? 'End' : 'Station ' + cur + ' of 7 · ' + name(cur);
    if (cur === GATE && !approved) label += ' · approve to continue';
    where.textContent = label;
    if (location.hash !== '#' + cur && history.replaceState) history.replaceState(null, '', cur ? '#' + cur : location.pathname);
  }
  function go(i, focus) {
    if (busy) return;
    i = Math.max(0, Math.min(LAST, i));
    if (i > GATE && !approved) {
      i = GATE;
      var a = stations[GATE].querySelector('.approve');
      stations[GATE].classList.add('nudge');
      setTimeout(function () { a.focus({ preventScroll: true }); }, 60);
    }
    if (i === cur) { paint(); return; }
    cur = i; paint();
    busy = true; setTimeout(function () { busy = false; }, reduced ? 50 : 750);
    if (focus !== false) setTimeout(function () { stations[cur].querySelector('h2').setAttribute('tabindex', '-1'); stations[cur].querySelector('h2').focus({ preventScroll: true }); }, reduced ? 0 : 400);
  }
  prev.addEventListener('click', function () { go(cur - 1); });
  next.addEventListener('click', function () { go(cur + 1); });
  dots.forEach(function (b) { b.addEventListener('click', function () { go(+b.dataset.go); }); });

  world.addEventListener('click', function (e) {
    var a = e.target.closest('.approve'); if (!a) return;
    approved = true; a.disabled = true; world.classList.add('approved');
    stations.forEach(function (s, i) { if (i > GATE) s.classList.add('unlocked'); });
    paint();
    setTimeout(function () { go(GATE + 1); }, reduced ? 0 : 900);
  });

  document.addEventListener('keydown', function (e) {
    if (body.classList.contains('flat')) return;
    var t = e.target; if (t && t.matches && t.matches('input,textarea,button,a') && e.key === ' ') return;
    if (e.key === 'ArrowDown' || e.key === 'PageDown' || e.key === ' ' || e.key === 'j') { e.preventDefault(); go(cur + 1); }
    else if (e.key === 'ArrowUp' || e.key === 'PageUp' || e.key === 'k') { e.preventDefault(); go(cur - 1); }
    else if (e.key === 'Home') { e.preventDefault(); go(0); }
    else if (e.key === 'End') { e.preventDefault(); go(LAST); }
  });
  var acc = 0, wheelT;
  document.addEventListener('wheel', function (e) {
    if (body.classList.contains('flat')) return;
    var s = stations[cur];
    // let a tall station scroll its own overflow first
    if (s.scrollHeight > s.clientHeight) {
      var atTop = s.scrollTop <= 0, atEnd = s.scrollTop + s.clientHeight >= s.scrollHeight - 1;
      if ((e.deltaY > 0 && !atEnd) || (e.deltaY < 0 && !atTop)) return;
    }
    e.preventDefault();
    acc += e.deltaY; clearTimeout(wheelT); wheelT = setTimeout(function () { acc = 0; }, 200);
    if (Math.abs(acc) > 60) { go(cur + (acc > 0 ? 1 : -1)); acc = 0; }
  }, { passive: false });
  var ty = null;
  document.addEventListener('touchstart', function (e) { ty = e.touches[0].clientY; }, { passive: true });
  document.addEventListener('touchend', function (e) {
    if (ty === null || body.classList.contains('flat')) return;
    var dy = ty - e.changedTouches[0].clientY; ty = null;
    if (Math.abs(dy) > 50) go(cur + (dy > 0 ? 1 : -1));
  }, { passive: true });

  // pointer parallax, off for touch and reduced motion
  if (!reduced && matchMedia('(hover: hover)').matches) {
    var stage = document.getElementById('stage');
    stage.addEventListener('pointermove', function (e) {
      var x = (e.clientX / innerWidth - .5) * 2, y = (e.clientY / innerHeight - .5) * 2;
      world.style.setProperty('transform', 'rotateX(' + (-y * 1.6) + 'deg) rotateY(' + (x * 2.2) + 'deg)');
    });
    stage.addEventListener('pointerleave', function () { world.style.removeProperty('transform'); });
  }

  function setFlat(on) {
    body.classList.toggle('flat', on);
    flatBtn.setAttribute('aria-pressed', on ? 'true' : 'false');
    flatBtn.textContent = on ? 'Corridor view' : 'Flat view';
    stations.forEach(function (s) { if (on) { s.removeAttribute('aria-hidden'); } });
    if (!on) paint();
    try { localStorage.setItem('level-flat', on ? '1' : '0'); } catch (e) {}
  }
  flatBtn.addEventListener('click', function () { setFlat(!body.classList.contains('flat')); });
  document.querySelector('.skip').addEventListener('click', function (e) { e.preventDefault(); setFlat(true); stations[0].querySelector('h2').focus(); });
  var wantFlat = false;
  try { wantFlat = localStorage.getItem('level-flat') === '1'; } catch (e) {}
  if (wantFlat || innerWidth < 380) setFlat(true);

  function fromHash() {
    var h = parseInt((location.hash || '').slice(1), 10);
    if (isNaN(h)) return false;
    cur = Math.min(Math.max(0, h), approved ? LAST : GATE);
    return true;
  }
  window.addEventListener('hashchange', function () { if (fromHash()) paint(); });
  fromHash();
  paint();
})();
