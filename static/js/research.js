$( document ).ready(function() {
  $("img").css("height", "");
  $("img").css("width", "");
  $('img').each(function() {
    if($(this).width()<=600)
    {
      $(this).addClass("ui large image");
    }
    else if($(this).width()<1200 && $(this).width()>600)
    {
      $(this).addClass("ui large image");
    }
    else if($(this).width()>1200)
    {
      $(this).addClass("ui huge image");
    }

  });
  $("table").addClass("ui stackable table")

});
