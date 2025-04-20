(function (window, document, $, undefined) {
  "use strict";

  /* Enter your custom scripts */

  // اضافه کردن کلاس active به لینک فعلی در منو
  $(document).ready(function () {
    var currentLocation = window.location.pathname;
    $(".c-header-1-nav a").each(function () {
      var linkLocation = $(this).attr("href");
      if (currentLocation.indexOf(linkLocation) !== -1) {
        $(this).addClass("active");
      }
    });

    // Fix for Contact us link on mobile
    $(".c-header-1-nav li.mega > a").on("click", function (e) {
      if ($(window).width() < 992) {
        // Allow the link to work normally on mobile
        return true;
      }
    });
  });
})(window, document, jQuery);
