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
          
          +"<div class='col-md-6'>"
          +"<form class='form-horizontal' role='form'>"
          
          +" <div class='form-group'> <label class='col-lg-2 control-label'>Nombres: </label><div class='col-lg-10'>"
          +"      <input type='text' class='form-control' id='inputEmail1' placeholder='Nombres' required "
          +"value='"+elemento.nombres+"''></div></div>"

          +" <div class='form-group'> <label class='col-lg-2 control-label'>Apellidos: </label><div class='col-lg-10'>"
          +"      <input type='text' class='form-control' id='inputEmail1' placeholder='Apellidos' required "
          +"value='"+elemento.apellidos+"''></div></div>"

          +" <div class='form-group'> <label class='col-lg-2 control-label'>Email: </label><div class='col-lg-10'>"
          +"      <input type='email' class='form-control' id='inputEmail1' placeholder='Email' required "
          +"value='"+elemento.email+"''></div></div>"

          +" <div class='form-group'> <label class='col-lg-2 control-label'>Telefono: </label><div class='col-lg-10'>"
          +"      <input type='number' class='form-control' id='inputEmail1' placeholder='Telefono' required "
          +"value='"+elemento.telefono+"''></div></div>"

          +" <div class='form-group'> <label class='col-lg-2 control-label'>Movil: </label><div class='col-lg-10'>"
          +"      <input type='number' class='form-control' id='inputEmail1' placeholder='Movil' required "
          +"value='"+elemento.mobil+"''></div></div>"

          +"<div class='form-group'><label class='col-lg-2 control-label'>Ciudad</label>"
          +"<div class='col-lg-10'><select id='mc' class='form-control'>"
          +elemento.ciudades 
          +"</select></div></div>"
          +"<div class='form-group'><div class='col-lg-offset-2 col-lg-10'>"
          +"<button type='button' class='btn btn-success'> "
          +" <span class='glyphicon glyphicon-save'></span>"
          +" Guardar Datos"
          +"</button> "        
          +" <button type='button' class='btn btn-warning'>"
          +"<span class='glyphicon glyphicon-remove-circle'></span>"
          +" Cancelar"
          +"</button>"
          +"</div></div></form></div>"

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



