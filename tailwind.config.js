/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './**/templates/**/*.html'
  ],
  theme: {
    extend: {
      colors: {
        'brand': '#CAB047',
        'brand-hv': '#D6BA49',
        'brand-light':'#FBF2D5',
        'brand-dark': '#7F6500',
      }
    },
  },
  plugins: [],
}

