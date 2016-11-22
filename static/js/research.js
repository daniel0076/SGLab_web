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
      $(this).addClass("ui medium image");
    }
    else if($(this).width()>1200)
    {
      $(this).addClass("ui big image");
    }

  });
  $("table").addClass("ui stackable table")

});
