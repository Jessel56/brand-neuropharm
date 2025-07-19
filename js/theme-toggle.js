/**
 * Handles the theme switching logic for Neuropharm Academy.
 * - Detects user's system preference.
 * - Checks for a saved preference in localStorage.
 * - Applies the correct theme on page load.
 * - Adds a click listener to the toggle button.
 */
document.addEventListener('DOMContentLoaded', () => {
  const THEME_STORAGE_KEY = 'neuropharm-theme';
  const htmlElement = document.documentElement;
  const toggleButton = document.querySelector('.theme-toggle');

  const getPreferredTheme = () => {
    const storedTheme = localStorage.getItem(THEME_STORAGE_KEY);
    if (storedTheme) {
      return storedTheme;
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  };

  const applyTheme = (theme) => {
    htmlElement.setAttribute('data-theme', theme);
    localStorage.setItem(THEME_STORAGE_KEY, theme);
  };

  if (toggleButton) {
    toggleButton.addEventListener('click', () => {
      const currentTheme = htmlElement.getAttribute('data-theme') || getPreferredTheme();
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      applyTheme(newTheme);
    });
  }

  // Apply the theme on initial load
  applyTheme(getPreferredTheme());
});
