/**
 * Handles the theme switching logic for Neuropharm Academy.
 * - Detects user's system preference.
 * - Checks for a saved preference in localStorage.
 * - Applies the correct theme on page load.
 * - Adds a click listener to the toggle button for three-way cycling.
 */
document.addEventListener('DOMContentLoaded', () => {
  const THEME_STORAGE_KEY = 'neuropharm-theme';
  const htmlElement = document.documentElement;
  const toggleButton = document.querySelector('.theme-toggle');

  const getPreferredTheme = () => {
    const storedTheme = localStorage.getItem(THEME_STORAGE_KEY);
    if (storedTheme && ['light', 'dim', 'dark'].includes(storedTheme)) {
      return storedTheme;
    }
    // Default to light if system preference is not dark
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  };

  const getNextTheme = (currentTheme) => {
    const themeOrder = ['light', 'dim', 'dark'];
    const currentIndex = themeOrder.indexOf(currentTheme);
    const nextIndex = (currentIndex + 1) % themeOrder.length;
    return themeOrder[nextIndex];
  };

  const applyTheme = (theme) => {
    htmlElement.setAttribute('data-theme', theme);
    localStorage.setItem(THEME_STORAGE_KEY, theme);
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
