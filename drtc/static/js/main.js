$(document).on('ready', dni  );

function dni(){
  $.ajaxSetup({
    beforeSend: function (xhr,settings){
      if(settings.type=="POST"){
        xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
      }
    }
  });

  $('#busca').on('click',buscar_dni); 

}
function buscar_dni(){
  var ndni = $('#dni').val();
  if(ndni != ''){
    $.get('busca-dni/'+ndni,ver_datos);
  }  
  else{
    alert('Ingrese un Valor');
  }
}

function ver_datos(data){
  var ul = $('#respuesta ul');
  ul.html('');
  $('#dni').val('');

  $.each(data.datos, function(i, elemento)){
    if (elemento.mensaje == 'no'){
      $(
        '<li>'
        +elemento.mensaje
        + ' '
        + elemento.apellidos
        + ' '
        + elemento.telefono
        + ' '
        + elemento.email
        + ' '
        + elemento.direccion       
        +'</li>'
        ).appendTo(ul);
    }
    else (elemento.mensaje == 'si'){
      $('<li>NO Exiiiistes :P </li>').appendTo(ul);
    }
  }
  });
}