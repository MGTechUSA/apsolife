/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html'
  ],
  theme: {
    extend: {
      colors: {
        'brand': '#D6BA49',
        'brand-hv': '#C5A82F',
        'brand-light':'#FBF2D5',
      }
    },
  },
  plugins: [],
}

