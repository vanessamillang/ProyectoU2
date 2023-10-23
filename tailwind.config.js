// tailwind.config.js
module.exports = {
  content: ["./movies/templates/**/*.html", "./movies/static/**/*.css"],
  theme: {
    extend: {
      spacing: {
        some_key: '6.5rem',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
};

