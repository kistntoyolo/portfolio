/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./*.html', './js/**/*.js'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', 'Inter', 'system-ui', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace'],
      },
      colors: {
        ink: {
          950: '#050816',
          900: '#0a0f24',
          800: '#10172f',
          700: '#182140',
          600: '#222d52',
        },
        electric: {
          300: '#7cc4ff',
          400: '#4da8ff',
          500: '#2b8cff',
          600: '#1a73f0',
        },
      },
      boxShadow: {
        glow: '0 0 0 1px rgba(77,168,255,.25), 0 10px 40px -10px rgba(43,140,255,.35)',
      },
    },
  },
  plugins: [],
};
