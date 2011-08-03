
/*hide the field from human users*/
$(document).ready(function(){

 $('#id_is_spam, #id_tricky').closest('tr, p').hide();
 $('.at-sign').html('@');
});
