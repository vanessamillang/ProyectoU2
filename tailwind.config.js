/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["*.html"],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Arial', 'sans'],
        mono: ['Courier New', 'monospace'],
      },
    },
  },
  plugins: [
    require ('@tailwind/forms'),
    require ('@tailwind/typography'),
  ],
}

