$(document).on('ready', dni  );
function dni(){
  $.ajaxSetup({
    beforeSend: function (xhr,settings){
      if(settings.type=="POST"){
        xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
      }
    }
  });

  $('#add_user').on('click',add_user);  
}

function add_user(){
	var datos=$("#add_usuario").serialize();
	$.post('/administrador',datos,
		function (data){

		},'json');
	return false;
}