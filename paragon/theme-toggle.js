/**
 * Theme Toggle Functionality for Neuropharm Academy
 * Handles light/dark mode switching with localStorage persistence
 */

(function () {
    'use strict';

    // Theme management
    const THEME_KEY = 'neuropharm-theme';
    const LIGHT_THEME = 'light';
    const DIM_THEME = 'dim';

    // Get current theme from localStorage or system preference
    function getCurrentTheme() {
        const savedTheme = localStorage.getItem(THEME_KEY);
        if (savedTheme) {
            return savedTheme;
        }
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? DIM_THEME : LIGHT_THEME;
    }

    // Apply theme to document
    function applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem(THEME_KEY, theme);

        // Update logo if present
        updateLogo(theme);
    }

    // Update logo based on theme
    function updateLogo(theme) {
        const logoContainers = document.querySelectorAll('.logo-container, .brand-logo-container');
        logoContainers.forEach(container => {
            const logoImg = container.querySelector('img');
            if (logoImg) {
                const logoSrc = theme === DIM_THEME ?
                    logoImg.src.replace('logo-light.svg', 'logo-dark.svg') :
                    logoImg.src.replace('logo-dark.svg', 'logo-light.svg');
                logoImg.src = logoSrc;
            }
        });
    }

    // Toggle theme
    function toggleTheme() {
        const currentTheme = getCurrentTheme();
        const newTheme = currentTheme === LIGHT_THEME ? DIM_THEME : LIGHT_THEME;
        applyTheme(newTheme);
    }

    // Create theme toggle button
    function createThemeToggle() {
        const toggleButton = document.createElement('button');
        toggleButton.className = 'theme-toggle';
        toggleButton.setAttribute('aria-label', 'Toggle dim mode');
        toggleButton.innerHTML = `
            <span class="icon-sun">☀️</span>
            <span class="icon-moon">🌙</span>
        `;

        toggleButton.addEventListener('click', toggleTheme);
        return toggleButton;
    }

    // Initialize theme on page load
    function initializeTheme() {
        const theme = getCurrentTheme();
        applyTheme(theme);

        // Add theme toggle to header or navigation
        const headerNav = document.querySelector('header nav, .navbar, .main-nav');
        if (headerNav) {
            const themeToggle = createThemeToggle();
            headerNav.appendChild(themeToggle);
        }
    }

    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem(THEME_KEY)) {
            applyTheme(e.matches ? DIM_THEME : LIGHT_THEME);
        }
    });

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializeTheme);
    } else {
        initializeTheme();
    }

    // Expose theme functions globally for external use
    window.NeuropharmTheme = {
        toggle: toggleTheme,
        getCurrent: getCurrentTheme,
        set: applyTheme
    };
})();
