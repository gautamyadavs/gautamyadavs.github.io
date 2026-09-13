document.querySelectorAll('[data-year]').forEach(element => {
  element.textContent = String(new Date().getFullYear());
});
const printButton = document.querySelector('[data-print]');
if (printButton) {
  printButton.hidden = false;
  printButton.addEventListener('click', () => window.print());
}
