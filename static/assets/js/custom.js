(function ( window, document, $, undefined ) {
	"use strict";

	/* Enter your custom scripts */

	// اضافه کردن کلاس active به لینک فعلی در منو
	$(document).ready(function() {
		var currentLocation = window.location.pathname;
		$('.c-header-1-nav a').each(function() {
			var linkLocation = $(this).attr('href');
			if (currentLocation.indexOf(linkLocation) !== -1) {
				$(this).addClass('active');
			}
		});
	});

})( window, document, jQuery );
