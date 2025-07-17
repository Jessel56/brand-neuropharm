/**
 * Neuropharm Academy Brand Package
 * Main entry point for the MFE brand customization
 */

// Import all brand assets
import './fonts.scss';
import './_variables.scss';
import './_overrides.scss';
import './theme-toggle.js';

// Brand configuration
export const NEUROPHARM_BRAND_CONFIG = {
    name: 'Neuropharm Academy',
    version: '1.0.0',
    theme: 'library-exclusive',
    modes: ['light', 'dark'],
    colors: {
        primary: '#B8860B',
        secondary: '#8B4513',
        accent: '#CD853F',
        parchment: '#F5F5DC',
        leather: '#6B4423'
    },
    fonts: {
        heading: 'Playfair Display',
        body: 'Crimson Text'
    },
    logos: {
        light: './logo-light.svg',
        dark: './logo-dark.svg'
    }
};

// Export theme utilities
export { NeuropharmTheme } from './theme-toggle.js';

// Default export
export default NEUROPHARM_BRAND_CONFIG;
