// Django entry point for the Gentelella v4 dashboard.
// CSS is loaded by the template, so this avoids the Vite-only SCSS import.

import { mountShell } from './v4/shell.js';
import { initCharts } from './v4/charts.js';
import { initTables } from './v4/tables.js';
import { openMenu, DEFAULT_CARD_MENU } from './v4/menus.js';
import { initCommandPalette } from './v4/command-palette.js';
import { initPageActions } from './v4/page-actions.js';

mountShell();
initCharts();
initTables();
initCommandPalette();
initPageActions();

if (document.getElementById('inbox-root')) {
  import('./v4/inbox.js').then((m) => m.initInbox());
}
if (document.querySelector('.calendar-grid')) {
  import('./v4/calendar.js').then((m) => m.initCalendar());
}
if (document.querySelector('.settings-content')) {
  import('./v4/settings.js').then((m) => m.initSettings());
}
if (document.querySelector('[data-date-range], [data-rich-text], [data-multi-select]')) {
  import('./v4/form-controls.js').then((m) => m.initFormControls());
}

document.addEventListener('click', (e) => {
  const toggle = e.target.closest('.toggle');
  if (toggle) {toggle.classList.toggle('on');}
});

document.addEventListener('click', (e) => {
  const cb = e.target.closest('.todo-cb');
  if (!cb) {return;}
  cb.classList.toggle('done');
  const row = cb.closest('.todo-row');
  if (row) {row.classList.toggle('done');}
  const card = cb.closest('.card');
  if (!card) {return;}
  const counter = card.querySelector('[data-todo-counter]');
  if (!counter) {return;}
  const all = card.querySelectorAll('.todo-row');
  const done = card.querySelectorAll('.todo-row.done');
  counter.textContent = `${all.length - done.length} of ${all.length} remaining`;
});

document.addEventListener('click', (e) => {
  const tab = e.target.closest('.chart-tab');
  if (!tab) {return;}
  tab.parentElement.querySelectorAll('.chart-tab').forEach((t) => t.classList.remove('active'));
  tab.classList.add('active');
});

document.addEventListener('click', (e) => {
  const btn = e.target.closest('.card-opt-btn');
  if (!btn || e.defaultPrevented) {return;}
  e.preventDefault();
  openMenu(btn, DEFAULT_CARD_MENU);
});

document.addEventListener('click', (e) => {
  const closer = e.target.closest('.chip-close');
  if (closer) {
    const chip = closer.closest('.chip');
    if (chip) {
      chip.style.transition = 'opacity 150ms, transform 150ms';
      chip.style.opacity = '0';
      chip.style.transform = 'scale(0.85)';
      setTimeout(() => chip.remove(), 160);
    }
    return;
  }
  const chip = e.target.closest('.chip');
  if (chip) {chip.classList.toggle('active');}
});

document.addEventListener('submit', (e) => {
  const form = e.target;
  if (!(form instanceof HTMLFormElement)) {return;}
  if (!form.matches('[data-js-submit]')) {return;}
  e.preventDefault();
  const submitBtn = form.querySelector('button[type="submit"], input[type="submit"]');
  const label = (submitBtn?.textContent || submitBtn?.value || 'Saved').trim();
  import('./v4/toast.js').then(({ showToast }) => showToast(`${label} OK`, { variant: 'success' }));
  if (form.dataset.resetOnSubmit !== 'false') {form.reset();}
});
