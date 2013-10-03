$(document).on('ready', dni  );

function dni(){
  $.ajaxSetup({
    beforeSend: function (xhr,settings){
      if(settings.type=="POST"){
        xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
      }
    }
  });

  $('#actualizar').on('click',buscar_dni);  
}

function buscar_dni(){
  var ndni = $('.navbar-form #dni').val();
  if(ndni != ''){
    if(ndni.length == 8){ 
      $.get('editar-dni/'+ndni,ver_datos);
      $('#respuesta').show();
    }
    else{
      alert('Formato de DNI: 8 Digitos');
      $('.navbar-form #dni').val(''); 
      $('#respuesta').hide();
    }    
  }  
  else{
    alert('Ingrese un Valor');
    $('.navbar-form #dni').val(''); 
    $('#respuesta').hide(); 
  }
}



function ver_datos(data){
  var hts = $('#respuesta');
  hts.html('');
  $('#dni').val('');
  $.each(data.dat, function(i, elemento){

    if(elemento.estado=='t'){
      $(
        "<div class='panel panel-default'>"
        +"<div class='panel-heading'>"
        +"<h3 class='panel-title'>"
        +"Modificar Datos Generales de Usuario"
        +"</h3>"
        +"</div>"
        +"<div class='panel-body'>" 
        +'<p>Numero de DNI: '+elemento.dni+"</p>"
        +"<button id='reguistra' data-toggle='modal'"
        +" href='#ModalCiudadano'  type='button' name='reguistrar' "
        +" class='btn btn-default btn-primary'>"
        +" <span class='glyphicon glyphicon-file'></span>"
        +" Nuevo Expediente"
        +"</button>"
        +"</div>"
        +"</div>"
        ).appendTo(hts)
    }
    else if(elemento.estado='f'){
      $(
        "<div class='panel panel-default'>"
        +"<div class='panel-heading'>"
        +"<h3 class='panel-title'>No Existen Datos de este DNI"
        +"</h3>"
        +"</div>"
        +"<div class='panel-body'>" 
        +"<a href='../' > Ir al Inicio</a>"
        +"</div>"
        +"</div>"
        ).appendTo(hts)

    }


  });
}



