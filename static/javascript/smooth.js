

/////////////////////////////

//////////////////////////////
// Make mobile navigation work

const menuButton = document.querySelector(".btn-mobile-nav");
const header = document.querySelector("header");
const openIdName = "nav--open";

function toggleNav() {
  if (header.getAttribute("id") === openIdName) {
    header.removeAttribute("id");
  } else {
    header.setAttribute("id", openIdName);
  }
}

menuButton.addEventListener("click", toggleNav);



///////////////////////////////////////////////////////////
// Smooth scrolling animation
