// Scoll Animation Using Jquery
$("#about-button").click(function() {
  $([document.documentElement, document.body]).animate({
    scrollTop: $("#about").offset().top
  }, 1000);
});

$("#pricing-button").click(function() {
  $([document.documentElement, document.body]).animate({
    scrollTop: $("#pricing").offset().top
  }, 1000);
});

$("#contactus-button").click(function() {
  $([document.documentElement, document.body]).animate({
    scrollTop: $("#contactus").offset().top
  }, 1000);
});
