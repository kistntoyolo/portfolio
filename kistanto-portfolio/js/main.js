/* Kistanto Portfolio - interaksi ringan tanpa dependensi */
(function () {
  'use strict';

  // Tahun footer
  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  // Navbar: latar saat scroll
  var navbar = document.getElementById('navbar');
  function onScroll() {
    if (!navbar) return;
    var scrolled = window.scrollY > 16;
    navbar.classList.toggle('bg-ink-950/85', scrolled);
    navbar.classList.toggle('backdrop-blur', scrolled);
    navbar.classList.toggle('border-white/10', scrolled);
    navbar.classList.toggle('border-transparent', !scrolled);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile hamburger menu
  var btn = document.getElementById('menu-btn');
  var menu = document.getElementById('mobile-menu');
  var iconOpen = document.getElementById('icon-open');
  var iconClose = document.getElementById('icon-close');

  function setMenu(open) {
    if (!btn || !menu) return;
    menu.classList.toggle('hidden', !open);
    iconOpen.classList.toggle('hidden', open);
    iconClose.classList.toggle('hidden', !open);
    btn.setAttribute('aria-expanded', String(open));
    btn.setAttribute('aria-label', open ? 'Tutup menu navigasi' : 'Buka menu navigasi');
  }
  if (btn && menu) {
    btn.addEventListener('click', function () {
      setMenu(btn.getAttribute('aria-expanded') !== 'true');
    });
    menu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { setMenu(false); });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') setMenu(false);
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth >= 768) setMenu(false);
    });
  }

  // Scroll reveal
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-visible'); });
  }

  // Active nav link (hanya di halaman utama)
  var sections = document.querySelectorAll('main section[id]');
  var links = document.querySelectorAll('header ul.hidden a.nav-link');
  if (sections.length && links.length && 'IntersectionObserver' in window) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          links.forEach(function (l) {
            l.classList.toggle('active', l.getAttribute('href') === '#' + entry.target.id);
          });
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach(function (s) { spy.observe(s); });
  }

  // Fallback foto profil: tampilkan inisial jika file foto belum ada
  var photo = document.getElementById('profile-photo');
  var fallback = document.getElementById('profile-fallback');
  if (photo && fallback) {
    var showFallback = function () {
      photo.classList.add('hidden');
      fallback.classList.remove('hidden');
      fallback.classList.add('grid');
    };
    photo.addEventListener('error', showFallback);
    if (photo.complete && photo.naturalWidth === 0) showFallback();
  }
})();
