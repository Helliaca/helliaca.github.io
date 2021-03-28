$(document).ready(function() {

    // When the client clicks a link
    $("a").click(function(event){

        // Get link location
        linkLocation = this.href;

        // If it directs to a page with the same domain
        if( location.hostname === this.hostname || !this.hostname.length ) {

            // Temporarily prevent it from directing there
            event.preventDefault();

            // Replace all fade-ins with fade-outs
            $('.fade-in-diag').removeClass('fade-in-diag').addClass('fade-out-diag');
            $('.fade-in').removeClass('fade-in').addClass('fade-out');

            // Wait some time, then redirect
            $('body').delay(100).queue(function(){
                // Note: We have to re-replace all fade-outs with fade-ins, because if the client hits the broweser "back"-button, the fade-outs will remain.
                $('.fade-out-diag').removeClass('fade-out-diag').addClass('fade-in-diag');
                $('.fade-out').removeClass('fade-out').addClass('fade-in');
                // We redirect the client now. Note: There is a second 1ms delay here because Firefox does some weird stuff when you hit the back-button and then click on a link
                $('body').delay(1).queue(function(){ window.location = linkLocation; }
            });
        }
    });
});
