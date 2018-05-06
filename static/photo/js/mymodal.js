
$("#triggerEvents").on("click", function(ev){
  ev.preventDefault();
  var modalid = $(this).data("target");
  var url = $(this).attr("href");

  $(modalid).modal("show"); // Triggering bootstrap modal.

  // Do the asynchronous part here.
});
