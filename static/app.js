const navToggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('#main-nav');

navToggle?.addEventListener('click', () => {
  const isOpen = navToggle.getAttribute('aria-expanded') === 'true';
  navToggle.setAttribute('aria-expanded', String(!isOpen));
  nav.classList.toggle('open', !isOpen);
});

nav?.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    navToggle?.setAttribute('aria-expanded', 'false');
    nav.classList.remove('open');
  });
});

const progress = document.querySelector('#reading-progress');
const updateProgress = () => {
  const available = document.documentElement.scrollHeight - window.innerHeight;
  const ratio = available > 0 ? window.scrollY / available : 0;
  if (progress) progress.style.transform = `scaleX(${Math.min(1, Math.max(0, ratio))})`;
};
window.addEventListener('scroll', updateProgress, { passive: true });
updateProgress();

const filters = [...document.querySelectorAll('.filter')];
const marchRows = [...document.querySelectorAll('.march-row')];
filters.forEach((button) => {
  button.addEventListener('click', () => {
    filters.forEach((item) => item.classList.remove('active'));
    button.classList.add('active');
    const filter = button.dataset.filter;
    marchRows.forEach((row) => {
      const show = filter === 'all' || row.dataset.troop === filter;
      row.hidden = !show;
    });
  });
});

const stageTabs = [...document.querySelectorAll('[role="tab"]')];
const stagePanels = [...document.querySelectorAll('[role="tabpanel"]')];

function activateStage(tab) {
  stageTabs.forEach((item) => {
    const active = item === tab;
    item.setAttribute('aria-selected', String(active));
    item.tabIndex = active ? 0 : -1;
  });
  stagePanels.forEach((panel) => {
    const active = panel.id === `panel-${tab.dataset.stage}`;
    panel.hidden = !active;
    panel.classList.toggle('active', active);
  });
}

stageTabs.forEach((tab, index) => {
  tab.addEventListener('click', () => activateStage(tab));
  tab.addEventListener('keydown', (event) => {
    if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;
    event.preventDefault();
    let nextIndex = index;
    if (event.key === 'ArrowRight') nextIndex = (index + 1) % stageTabs.length;
    if (event.key === 'ArrowLeft') nextIndex = (index - 1 + stageTabs.length) % stageTabs.length;
    if (event.key === 'Home') nextIndex = 0;
    if (event.key === 'End') nextIndex = stageTabs.length - 1;
    stageTabs[nextIndex].focus();
    activateStage(stageTabs[nextIndex]);
  });
});

const revealItems = document.querySelectorAll('.reveal');
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -40px' });
  revealItems.forEach((item) => observer.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add('visible'));
}

