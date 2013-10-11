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
  $('#add_clinica').on('click',add_clinica);  
  $('#add_escuela').on('click',add_escuela);  
  $('#add_lugar').on('click',add_lugar);  
}

function add_user(){
  var datos=$("#add_form_user").serialize();
  $.post('/administrador',datos,
    function (data){
    },'json');
  return false;
}

function add_clinica(){
  var datos=$("#add_form_clinica").serialize();
  $.post('/administrador',datos,
    function (data){
    },'json');
  return false;
}

function add_escuela(){
  var datos=$("#add_form_escuela").serialize();
  $.post('/administrador',datos,
    function (data){
    },'json');
  return false;
}

function add_lugar(){
	var datos=$("#add_form_lugar").serialize();
	$.post('/administrador',datos,
		function (data){
		},'json');
	return false;
}