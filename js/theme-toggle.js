/**
 * Handles the theme switching logic for Neuropharm Academy.
 * - Detects user's system preference.
 * - Checks for a saved preference in localStorage.
 * - Applies the correct theme on page load.
 * - Cycles through light → dim → dark → light themes.
 */
document.addEventListener('DOMContentLoaded', () => {
  const THEME_STORAGE_KEY = 'neuropharm-theme';
  const htmlElement = document.documentElement;
  const toggleButton = document.querySelector('.theme-toggle');
  
  // Theme cycle: light → dim → dark → light
  const THEME_CYCLE = ['light', 'dim', 'dark'];

  const getPreferredTheme = () => {
    const storedTheme = localStorage.getItem(THEME_STORAGE_KEY);
    if (storedTheme && THEME_CYCLE.includes(storedTheme)) {
      return storedTheme;
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  };

  const applyTheme = (theme) => {
    htmlElement.setAttribute('data-theme', theme);
    localStorage.setItem(THEME_STORAGE_KEY, theme);
  };

  const getNextTheme = (currentTheme) => {
    const currentIndex = THEME_CYCLE.indexOf(currentTheme);
    const nextIndex = (currentIndex + 1) % THEME_CYCLE.length;
    return THEME_CYCLE[nextIndex];
  };

  if (toggleButton) {
    toggleButton.addEventListener('click', () => {
      const currentTheme = htmlElement.getAttribute('data-theme') || getPreferredTheme();
      const newTheme = getNextTheme(currentTheme);
      applyTheme(newTheme);
    });
  }

  // Apply the theme on initial load
  applyTheme(getPreferredTheme());
});
