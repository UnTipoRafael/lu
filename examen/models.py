# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User



# Create your models here.

class Lugar(models.Model):
	nombres 			=models.CharField(max_length=200)
	direccion			=models.CharField(max_length=200)
	telefono			=models.CharField(max_length=200)

	def __unicode__(self):
		return self.nombres

class Escuela(models.Model):
	nombre 				=models.CharField(max_length=200)
	direccion			=models.CharField(max_length=200)
	telefono			=models.CharField(max_length=200)
	email				=models.EmailField(blank=True
)
	
	def __unicode__(self):
		return self.nombre

class Clinica(models.Model):
	nombre 				=models.CharField(max_length=200)
	direccion			=models.CharField(max_length=200)
	telefono			=models.CharField(max_length=200)
	email				=models.EmailField(blank=True
)
	
	def __unicode__(self):
		return self.nombre

class Perfil(models.Model):
	user = models.ForeignKey(User)
	registrador= 're'
	evaluador = 'ev'
	administrador ='ad'
	programador ='po'
	roles= (
		(registrador, 'Registrador'),
		(evaluador, 'Evaluador'),
		(programador, 'Programador'),
		(administrador, 'Administrador'),
	)

	rol					=models.CharField(max_length=2,
										choices=roles,
										default=(registrador))		

	contrato_ingreso	=models.DateField(blank=True
)
	contrato_salida		=models.DateField(blank=True
)
	telefono			=models.CharField(max_length=200, blank=True
)
	dni					=models.CharField(max_length=200)
	direccion			=models.CharField(max_length=200, blank=True
)

	def __unicode__(self):
		return str(self.user.id)+" > "+self.rol

class Ciudadano(models.Model):
	nombres 			=models.CharField(max_length=200)
	apellidos			=models.CharField(max_length=200)
	dni					=models.CharField(max_length=8, unique=True)
	telefono			=models.CharField(max_length=10)
	mobil				=models.CharField(max_length=10)
	fecha_nacimiento	=models.DateField()
	direccion			=models.CharField(max_length=200)
	email				=models.EmailField()

	def __unicode__(self):
		return self.nombres

class Registro(models.Model): 
	numero_registro		=models.IntegerField()
	numero_expediente	=models.IntegerField()
	id_ciudadano		=models.ForeignKey(Ciudadano)
	id_usuario			=models.ForeignKey(Perfil)
	id_clinica			=models.ForeignKey(Clinica)
	fecha_examen_medico =models.DateField()
	asunto				=models.CharField(max_length=10)
	
	def __unicode__(self):
		return str(self.numero_registro)


class Programacion(models.Model):
	manejo= 'MA'
	reglas = 'RE'
	tipo = (
        (manejo, 'Manejo'),
        (reglas, 'Reglas'),
    )

	id_ciudadano		=models.ForeignKey(Ciudadano)
	fecha 				=models.DateField()
	intentos			=models.IntegerField()
	id_lugar			=models.ForeignKey(Lugar)
	tipo				=models.CharField(max_length=2,
                                      choices=tipo,
                                      default=(reglas))	
	fecha_log			= models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return str(self.id_ciudadano)

class Preguntas(models.Model):
	manejo= 'MA'
	reglas = 'RE'
	tipo = (
        (manejo, 'Manejo'),
        (reglas, 'Reglas'),
    )

	pregunta 			=models.CharField(max_length=400)
	id_alternativa		=models.IntegerField()
	tipo 				=models.CharField(max_length=2,
                                      choices=tipo,
                                      default=(reglas))
	def __unicode__(self):
		return str(self.pregunta)

class Respuestas(models.Model):
	alternativa 		=models.CharField(max_length=400)
	id_pregunta 		=models.IntegerField()

	def __unicode__(self):
		return str(self.alternativa)

class Examen(models.Model):
	id_ciudadano		=models.ForeignKey(Ciudadano)
	fecha 				=models.DateField()
	ip_maquina			=models.CharField(max_length=50)
	detalle 			=models.CharField(max_length=600)
	nota				=models.IntegerField()
	fecha_log			=models.DateField(auto_now=True, auto_now_add=True ,editable=False, blank=True)
