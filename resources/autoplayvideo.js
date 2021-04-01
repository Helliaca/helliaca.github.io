$(document).ready(function() {
  $(".preview-video").on("mouseover", function(event) {
    this.play();

  }).on('mouseout', function(event) {
    this.pause();

  });
})
