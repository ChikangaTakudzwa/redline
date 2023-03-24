/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    colors: {
      redline: '#B10000',
      secondary: colors.lightBlue,
    },
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
