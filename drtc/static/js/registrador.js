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
  $('#programa').on('click',programa_dni); 


}

function programa_dni(){
  var ndni = $('#dni').val();
  $.get('programa-dni/'+ndni, programar_datos);
}

function programar_datos(data){
  var hts = $('#respuestaprogramacion');
  hts.html('');
  $('#dni').val('');
  $.each(data.datosprograma, function(i,elemento){

    if(elemento.mensaje=='No'){
      $("<div class='panel panel-danger'>"
        +"<div class='panel-heading'>"
        +"<h3 class='panel-title'> No tiene Registros"
        + " - Intentos: - " 
        +"</h3>"
        +"</div>"
        +"<div class='panel-body'>" 
        +"<form>"
        +"<label>Fecha de Examen</label><input type='date' >"
        +"<label>Lugar</label><select></select>"
        +"</form>"
        +"</div>"
        +"</div>").appendTo(hts);
    }
    else{ 
      $("<div class='panel panel-default'>"
        +"<div class='panel-heading'>"
        +"<h3 class='panel-title'>"
        +elemento.nombres+  " - Intentos: " +elemento.intentos
        +"</h3>"
        +"</div>"
        +"<div class='panel-body'>"
        +"<input type='hidden' id='ic' value='"+elemento.idpersona+"'>"
        +"<label>Fecha:</label><input id='fecha_examen' type='date'/>"
        +"<label>Lugar:</label><select id='id_lugar'> <option value='1'>DRTC</option> <option value='2'>ORIO</option> </select>"
        +"<label>Tipo:</label><select id='tipo'> <option value='1'>Manejo</option> <option value='2'>Reglas</option> </select>"
        +"<button id='reprograma' class='btn btn-primary'> Re-Programar </button>"
        +"</div>"
        +"</div>").appendTo(hts);
      }

  });
}
 


function buscar_dni(){
  var ndni = $('#dni').val();
  if(ndni != ''){
    if(ndni.length == 8){
      $.get('busca-dni/'+ndni,ver_datos);
      $('#respuesta').show();
    }
    else{
      alert('Formato de DNI: 8 Digitos');
      $('#dni').val(''); 
      $('#respuesta').hide();
    }    
  }  
  else{
    alert('Ingrese un Valor');
    $('#dni').val(''); 
    $('#respuesta').hide(); 
  }
}

function ver_datos(data){
  var hts = $('#respuesta');
  hts.html('');
  $('#dni').val('');
  $.each(data.datos, function(i, elemento){ 
    $(
      "<div class='panel panel-default'>"
      +"<div class='panel-heading'>"
      +"<h3 class='panel-title'>"
      +elemento.nombres+ " " +elemento.apellidos
      +"</h3>"
      +"</div>"
      +"<div class='panel-body'>"
      +"Email: "+elemento.email+ " Telefono: " +elemento.telefono
      +"</div>"
      +"</div>").appendTo(hts);
  });
}