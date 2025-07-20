/**
 * Theme Toggle Functionality for Neuropharm Academy
 * Handles light/dim mode switching with localStorage persistence
 */

(function() {
    'use strict';

    // Theme constants
    const THEME_KEY = 'neuropharm-theme';
    const LIGHT_THEME = 'light';
    const DIM_THEME = 'dim';
    
    // DOM elements
    let themeToggleButton = null;
    let documentElement = null;

    /**
     * Get the current theme from localStorage or default to light
     * @returns {string} Current theme ('light' or 'dim')
     */
    function getCurrentTheme() {
        const savedTheme = localStorage.getItem(THEME_KEY);
        
        // Return saved theme if it exists and is valid
        if (savedTheme && (savedTheme === LIGHT_THEME || savedTheme === DIM_THEME)) {
            return savedTheme;
        }
        
        // Default to light theme
        return LIGHT_THEME;
    }

    /**
     * Apply theme to the document
     * @param {string} theme - Theme to apply ('light' or 'dim')
     */
    function applyTheme(theme) {
        if (!documentElement) {
            documentElement = document.documentElement;
        }

        // Validate theme
        if (theme !== LIGHT_THEME && theme !== DIM_THEME) {
            console.warn('Invalid theme:', theme, 'defaulting to light');
            theme = LIGHT_THEME;
        }

        // Apply theme to document
        documentElement.setAttribute('data-theme', theme);
        
        // Save to localStorage
        localStorage.setItem(THEME_KEY, theme);

        // Update toggle button if it exists
        updateToggleButton(theme);

        // Dispatch custom event for other components to listen to
        const themeChangeEvent = new CustomEvent('themeChanged', {
            detail: { theme: theme }
        });
        document.dispatchEvent(themeChangeEvent);

        console.log('Theme applied:', theme);
    }

    /**
     * Update the toggle button appearance based on current theme
     * @param {string} theme - Current theme
     */
    function updateToggleButton(theme) {
        if (!themeToggleButton) return;

        // Update aria-label for accessibility
        const newLabel = theme === LIGHT_THEME 
            ? 'Switch to dim theme' 
            : 'Switch to light theme';
        
        themeToggleButton.setAttribute('aria-label', newLabel);

        // Icons are handled via CSS, but we can add data attribute for additional styling
        themeToggleButton.setAttribute('data-current-theme', theme);
    }

    /**
     * Toggle between light and dim themes
     */
    function toggleTheme() {
        const currentTheme = getCurrentTheme();
        const newTheme = currentTheme === LIGHT_THEME ? DIM_THEME : LIGHT_THEME;
        
        console.log('Toggling theme from', currentTheme, 'to', newTheme);
        applyTheme(newTheme);
    }

    /**
     * Initialize the theme system
     */
    function initializeTheme() {
        console.log('Initializing theme system');
        
        // Get DOM elements
        documentElement = document.documentElement;
        themeToggleButton = document.getElementById('theme-toggle');

        if (!themeToggleButton) {
            console.warn('Theme toggle button not found. Make sure element with id="theme-toggle" exists.');
            return;
        }

        // Apply saved theme or default
        const savedTheme = getCurrentTheme();
        console.log('Initial theme:', savedTheme);
        applyTheme(savedTheme);

        // Add click event listener to toggle button
        themeToggleButton.addEventListener('click', (e) => {
            e.preventDefault();
            toggleTheme();
        });

        // Add keyboard support (Enter and Space)
        themeToggleButton.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                toggleTheme();
            }
        });

        // Listen for system theme preference changes (optional enhancement)
        if (window.matchMedia) {
            const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
            mediaQuery.addEventListener('change', (e) => {
                // Only auto-switch if no theme is saved in localStorage
                if (!localStorage.getItem(THEME_KEY)) {
                    // Note: We map system dark preference to our 'dim' theme
                    const systemTheme = e.matches ? DIM_THEME : LIGHT_THEME;
                    console.log('System theme preference changed to:', systemTheme);
                    applyTheme(systemTheme);
                }
            });
        }

        console.log('Theme system initialized successfully');
    }

    /**
     * Public API for external access
     */
    const NeuropharmTheme = {
        /**
         * Toggle between light and dim themes
         */
        toggle: toggleTheme,
        
        /**
         * Get the current theme
         * @returns {string} Current theme
         */
        getCurrent: getCurrentTheme,
        
        /**
         * Set a specific theme
         * @param {string} theme - Theme to set ('light' or 'dim')
         */
        set: applyTheme,
        
        /**
         * Available themes
         */
        themes: {
            LIGHT: LIGHT_THEME,
            DIM: DIM_THEME
        }
    };

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializeTheme);
    } else {
        // DOM is already loaded
        initializeTheme();
    }

    // Expose public API globally
    window.NeuropharmTheme = NeuropharmTheme;

    // Also expose individual functions for backward compatibility
    window.toggleTheme = toggleTheme;
    window.getCurrentTheme = getCurrentTheme;
    window.setTheme = applyTheme;

})();