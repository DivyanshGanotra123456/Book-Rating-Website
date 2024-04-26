$(function () {

   
    var galleryImage = $("#wrapper").find("img").first();
  
   
    var images = [
      "img/back1.jpg",
      "img/back2.jpg",
      "img/back3.jpg",
      "img/back4.jpg"
    ];
  
    
    var i = 0;
  
    setInterval(function() {
      
      i = (i + 1) % images.length;  
  
     
      galleryImage.fadeOut(function() {
        
        $(this).attr("src", images[i]);
        $(this).fadeIn();
      });
  
      
      console.log(galleryImage.attr("src"));
  
    }, 2000);
  
  });