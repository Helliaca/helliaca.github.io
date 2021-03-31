$(document).ready(function() {

    // When the client clicks a link
    $("a").click(function(event){

        // Get link location
        linkLocation = this.href;

        // If it directs to a page with the same domain
        if( !$(this).hasClass("no-fade") && (location.hostname === this.hostname || !this.hostname.length )) {

            // Temporarily prevent it from directing there
            event.preventDefault();

            // Replace all fade-ins with fade-outs
            $('.fade-in-diag').removeClass('fade-in-diag').addClass('fade-out-diag');
            $('.fade-in').removeClass('fade-in').addClass('fade-out');

            // Wait some time, then redirect
            $('body').delay(100).queue(function(){
                window.location = linkLocation;
            });
        }
    });
});
