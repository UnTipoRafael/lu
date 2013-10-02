# -*- coding: utf-8 -*-
import json
from datetime import datetime, date
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse, Http404
from django.contrib.auth.decorators import login_required
#modelos
from examen.models import Ciudadano, Examen, Programacion, Registro
#form
from examen.form import form_login, form_user, CiudadanoForm , ProgramacionForm

def inicio(request):
	if request.user.is_authenticated():
		grupo	= 	request.user.groups.all()[0].name 
		
		if grupo=='registrador':
			return HttpResponseRedirect('/registrador')

		elif grupo=='evaluador':
			return HttpResponseRedirect('/evaluador')

		elif grupo=='administrador':
			return HttpResponseRedirect('/administrador')
			#return render_to_response('administrador.html',{},context_instance=RequestContext(request))

		elif grupo=='programador':
			return HttpResponseRedirect('/programador')
			#return render_to_response('programador.html',{},context_instance=RequestContext(request))

		elif grupo=='administrador':
			return HttpResponseRedirect('/administrador')
			#return render_to_response('administrador.html',{},context_instance=RequestContext(request))

		elif grupo=='ciudadano':
			return HttpResponseRedirect('/ciudadano')
			#return render_to_response('ciudadano.html',{},context_instance=RequestContext(request))
		
		else :
			return HttpResponseRedirect('/')	
	else:
		return render_to_response('index.html',{},context_instance=RequestContext(request))

def ingreso(request):
	if request.method=='POST':
		form_usuario	=	request.POST['usuario']
		form_password	=	request.POST['password']
		acceso			=	authenticate(username=form_usuario,password=form_password)
		
		if acceso is not None:

			if acceso.is_active:
				login(request, acceso)
				return HttpResponseRedirect('/')
				
			else:
				mensaje='El usuario no esta activo'
				return render_to_response('index.html',{'mensaje':mensaje},context_instance=RequestContext(request))
		else:
			mensaje='No existe el usuario'
			return render_to_response('index.html',{'mensaje':mensaje},context_instance=RequestContext(request))		
	else:
		f_login = form_login();
		return render_to_response('index.html',{'form':f_login},context_instance=RequestContext(request))

'''def reprograma_dni(request,ic,f,il,t):
	#pregunta = Preguntas(titulo=request.POST['pregunta'])
	if request.is_ajax():
		p = Programacion.objects.filter(id_ciudadano=ic).order_by('-fecha_log')
		qint = p[0].intentos - 1

		reprograma = Programacion(id_ciudadano=ic,fecha=f,intentos=qint,tipo=t,fecha_log=datetime.now()) 
		reprograma.save()

		data.append({
			'mensaje': 'ok', 
			})	

		return HttpResponse(
			json.dumps({'datosreprograma':data}),
			content_type="application/json; charset=utf8"
			)
	else:
		raise Http404
'''
def programa_dni(request,ndni):
	if request.is_ajax():
		datosdni = Ciudadano.objects.filter(dni=ndni)
		data = list()
		idcito = '' 
		for i in datosdni:
			idcito = i.pk
		
		programa = Programacion.objects.filter(id_ciudadano = idcito).order_by('-fecha_log')
		q_resul= len(programa)
		if (q_resul==0):
			data.append({
				'mensaje': 'No'
				})
		else: 
			elegido = programa[0] 
			data.append({
				'idpersona': str(idcito),
				'intentos' : str(elegido.intentos),
				'nombres' : str(elegido.id_ciudadano),
				'lugar' : str(elegido.id_lugar),
				})

		return HttpResponse(
			json.dumps({'datosprograma':data}),
			content_type="application/json; charset=utf8"
			)
	else:
		raise Http404	


"""
for i in p:
...     if (i.fecha > date.today()):
...         print '1 fe es mayor'
...     elif(date.today()>i.fecha):
...         print '2 fe es mayor'
...     else:
...         print 'error'

"""

def busca_dni(request,ndni):
	if request.is_ajax(): 
		# Busqueda de un ciudadano aqui mediante el DNI
		datosdni = Ciudadano.objects.filter(dni=ndni)
		mensaje = ''
		data = list()
		# Esta cantidad debe ser 1 y se verifica que se tiene a un usuario
		# con el que trabajaremos y buscaremos datos si no enviar mensaje
		# de que no se encuentra y se mandara al reguistro
		q = len(datosdni) # 1/0 

		if q == 1:
			mensaje = 'si'
			for dato in datosdni:
				pp = Programacion.objects.filter(id_ciudadano=dato.id)
				if (len(pp) == 0):
					#no existe algo programado mandar boton NExpediente
					mensaje = 'no existe y BOTON NEXPEDIENTE'
					data.append({  
						'mensaje': mensaje,
					})
				elif(len(pp)>0):
					#existen muchos rows programados cogemos el -pk[0] (ultimo)
					ultimo = pp.order_by('-pk')[0]
					intentos = ultimo.intentos
					idpro = ultimo.pk
					pr = Registro.objects.filter(id_programacion=idpro)
					for i in pr:
						if (i.fecha_examen_medico > date.today()):
							# Su examen aun es valido
							if(intentos == 0):
								# datos de su ultimo examen 
								# y botonNExpediente
								mensaje = 'ult Intento+fecha de examen / BOTON NEXPEDIENTE'
								data.append({  
									'mensaje': mensaje,
								})
							elif(intentos >=1 & intentos <=2 ):
								# Dato  examen 
								# y Boton NRegistros
								mensaje = 'tienes 2/1 intentos datos/ NREGISTRO'
								data.append({  
									'mensaje': mensaje,
								})

						elif(i.fecha_examen_medico < date.today() or i.fecha_examen_medico == date.today() ):
							# Su examen ya vencio/ NExpediente
							mensaje = 'EXAMEN MEDICO VENCIO / NEXPEDIENTE'
							data.append({  
								'mensaje': mensaje,
							})

			"""
			for dato in datosdni:				
				data.append({  
					'mensaje': mensaje,
					'idcito': dato.id,
					'fechaexamen': str(pp.fecha),
					'nombrecompleto': dato.nombres+" "+dato.apellidos,
					})
			"""


		else:
			mensaje = 'no'
			data.append({  
				'mensaje': mensaje,
				})

		 


		return HttpResponse(
			json.dumps({'datos':data}),
			content_type="application/json; charset=uft8"
			)
	else:
		raise Http404


#@login_required
def salir(request):
	logout(request)
	return HttpResponseRedirect('/')


@login_required(login_url='/')
def registrador(request):
	grupo	= 	request.user.groups.all()[0].name 
	if grupo=='registrador':
		data = {}
		# AGREGA CIUDADANO
		if request.method == "POST":
			ciudadano = CiudadanoForm(request.POST)
			if ciudadano.is_valid():
				ciudadano.save()
				return HttpResponseRedirect('/')
			else:
				data['mensaje'] = "No Ingreso Ciudadado"
		data['Form_Ciu'] = CiudadanoForm()
		# AGREGA CIUDADANO
		return render_to_response('registrador.html',data,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')
		
@login_required(login_url='/')
def evaluador(request):
	grupo	= 	request.user.groups.all()[0].name 
	if grupo=='evaluador':
		data={}
		data['evaluados'] = Examen.objects.all() 
		return render_to_response('evaluador.html',data,context_instance=RequestContext(request))

	else:
		return HttpResponseRedirect('/')

@login_required(login_url='/')
def administrador(request):
	grupo= request.user.groups.all()[0].name 
	if grupo=='administrador':
		form_add=form_user()
		return render_to_response('administrador.html',{'form':form_add},context_instance=RequestContext(request))

	else:
		return HttpResponseRedirect('/')

#def add_usuario(request):
def test(request):
	form_add=form_user()
	print form_add
	if request.method=='POST':

		usuario 	=request.POST['user']
		password 	=request.POST['password']
		active 		=request.POST['active']
		nombre 		=request.POST['fistname']
		apellido 	=request.POST['lastname']
		dni 		=request.POST['dni']
		email 		=request.POST['email']
		grupo 		=request.POST['group']

		contrato_ingreso 	=request.POST['contrato_ingreso']
		contrato_salida 	=request.POST['contrato_salida']
		telefono 			=request.POST['telefono']
		direccion 			=request.POST['direccion']

		user 				= User.objects.create_user(usuario, email, password)

		if usuario and email and password:
			user.save()
			queryset=User.objects.all().get(dni=dni)

			msg='Usuario no añadido'
			print msg
		return HttpResponseRedirect('/')

	else:
		return render_to_response('add_usuario.html',{'form':form_add},context_instance=RequestContext(request))

@login_required(login_url='/')
def evaluado(request):
	grupo= request.user.groups.all()[0].name 
	if grupo=='evaluado':
		form_add=form_user()
		return render_to_response('evaluado.html')
	else:
		return HttpResponseRedirect('/')
	
@login_required(login_url='/')
def ciudadano(request):
	grupo= request.user.groups.all()[0].name 
	if grupo=='ciudadano':
		form_add=form_user()
		return render_to_response('ciudadano.html')
	else:
		return HttpResponseRedirect('/')

def programador(request):
	grupo= request.user.groups.all()[0].name 
	if grupo=='programador':
		form_add=form_user()
		return render_to_response('programadni.html')
	else:
		return HttpResponseRedirect('/')

def busqueda(request):
	return render_to_response('index.html')


def info(request):
	return render_to_response('index.html')