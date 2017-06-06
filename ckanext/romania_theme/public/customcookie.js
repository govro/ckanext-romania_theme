$(document).ready(function(){
  if ($.cookie('modal_shown') == null) {
    $.cookie('modal_shown', 'yes', { expires: 1, path: '/' });
    $('#id01').reveal();
  }
});