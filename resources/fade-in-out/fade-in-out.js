$(document).ready(function() {
    $("a").click(function(event){
        linkLocation = this.href;
        if( location.hostname === this.hostname || !this.hostname.length ) {
            event.preventDefault();
            $('.fade-in-diag').removeClass('fade-in-diag').addClass('fade-out-diag');
            $('.fade-in').removeClass('fade-in').addClass('fade-out');
            $('body').delay(100).queue(function(){
                window.location = linkLocation;
            });
        }
    });
});
