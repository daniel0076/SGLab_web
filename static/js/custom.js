
$( document ).ready(function() {
  $('.ui.sticky').sticky({
    offset       : 100,
    bottomOffset : 50,
    context      : '#wrapper',
    onStick: function(){
      $('.ui.sticky').css('display','');
    },
    onTop: function(){
      $('.ui.sticky').css('display','none');
    },
  }) ;

});
