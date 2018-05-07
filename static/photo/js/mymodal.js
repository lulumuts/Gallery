$(document).ready(function () {
  // var this_m = $('button#trigger-modal')
 var $this_image = $('#each-image')
$this_image.each(function(){

  var this_m = $('button#trigger-modal')

   this_m.on('click', function () {
     var image = $(this).data('url');
     var image_name = $(this).data('image-name');
     var image_description = $(this).data('description');
     var image_location = $(this).data('location');
     

       //alert(image);

       $('#myModal').on('show.bs.modal', function () {
         $("#myModal").find("#modal-image").attr("src",image);
           var obj = $("#myModal").find("#myModalLabel").text("IMAGE NAME: "+image_name+"\n IMAGE DESCRIPTION:"+image_description+"\n IMAGE LOCATION:"+image_location)

           obj.html(obj.html().replace(/\n/g,'<br/>'))


       });
   });
 })
});
