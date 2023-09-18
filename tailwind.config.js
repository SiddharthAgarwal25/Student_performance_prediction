module.exports = {
  content: [
    './templates/**/*.html', // Adjust the path as needed
  ],
  purge: {
    enabled: true,
    content: ['./templates/**/*.html'], // Match the content paths above
  },
  theme: {
    extend: {},
  },
  plugins: [],
}
