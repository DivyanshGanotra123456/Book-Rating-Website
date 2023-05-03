var images = [
  "../static/images/books.jpg",
  "../static/images/bg3.jpg",
  "../static/images/bg5.jpg",
];
function slideshow() {
  var i = 0;
  setInterval(function () {
    i++;
    if (i == images.length) {
      i = 0;
    }
    $("#slideshow").css("background-image", "url(" + images[i] + ")");
  }, 2000);
}
$(document).ready(function () {
  slideshow();
});
