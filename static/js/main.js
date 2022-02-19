
function openNav() {
  document.getElementById("navLinks").style.right = "0px";
}

function closeNav() {
  document.getElementById("navLinks").style.right = "-200px";
}



$(document).ready(function(){
$('.course-slider').slick({
  autoplay:true,
  slidesToShow:3,
  slidesToScroll:1,
  prevArrow:".prev-btn",
  nextArrow:".next-btn",
  responsive:[
    {
      breakpoint:992,
      settings:{
      slidesToShow:2,}},
         {
          breakpoint:768,
          settings:{
           slidesToShow:1,
          }
       }]
});
$('.facilities-slider').slick({
  autoplay:true,
 slidesToShow:3,
 slidesToScroll:1,
 prevArrow:".prev-btn",
 nextArrow:".next-btn",
 responsive:[
    {
       breakpoint:992,
       settings:{
        slidesToShow:2,
       }
    },
    {
     breakpoint:768,
     settings:{
      slidesToShow:1,
     }
  }
 ]
  });
});


// Nút cuộn lên top

$(document).ready(function(){
  $(window).scroll(function(event){
    var pos_body = $('html,body').scrollTop();
    
    if(pos_body>20){
      $('.header-menu').addClass('sticky');
    }
    else{
      $('.header-menu').removeClass('sticky');
    }
    if(pos_body>800){
      $('.scrollToTop').addClass('show-scroll');
    }
    else{
      $('.scrollToTop').removeClass('show-scroll');
    }
  });
  
  $('.scrollToTop').click(function(event){
    $('html,body').animate({
        scrollTop:0},600);
      });
    });

      

  $(document).ready(function(){

      $('.buttons').click(function(){
  
          $(this).addClass('active').siblings().removeClass('active');
  
          var filter = $(this).attr('data-filter')
  
          if(filter == 'all'){
              $('.image').show(400);
          }else{
              $('.image').not('.'+filter).hide(200);
              $('.image').filter('.'+filter).show(400);
          }
  
      });
  
      $('.gallery').magnificPopup({
  
          delegate:'a',
          type:'image',
          gallery:{
              enabled:true
          }
      });
  
  });




