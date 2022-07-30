/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        pDrak: "#333333",
        pBgDark: "#444444",
        pWhite: "#F6F6F6",
        pGray: "#E8E8E8",
        pDarkRed: "#990100",
        pRed: "#B90504",
      },
    },
  },
  plugins: [],
};
