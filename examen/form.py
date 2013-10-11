# -*- coding: utf-8 -*-
from django import forms

from django.contrib.auth.models import User, Group
from django.forms import ModelForm 
from examen.models import Ciudadano ,Programacion ,Perfil, Escuela, Clinica, Lugar
from django.forms.widgets import TextInput, DateInput, DateTimeInput, TimeInput ,HiddenInput
import datetime

class MyEmailInput(TextInput):
    input_type = 'email'

class MyNumberInput(TextInput):
    input_type = 'number'

class MyTelephoneInput(TextInput):
    input_type = 'tel'

class MyDateInput(DateInput):
    input_type = 'date'

class MyDateTimeInput(DateTimeInput):
    input_type = 'datetime'

class MyTimeInput(TimeInput):
    input_type = 'time'


class form_login(forms.Form):
    usuario		= forms.CharField(max_length=100)
    password	= forms.CharField()

class CiudadanoForm(ModelForm):
    class Meta:
        model = Ciudadano 
 
        widgets = {
            'nombres': TextInput(attrs={'class':'form-control'}),
            'apellidos': TextInput(attrs={'class':'form-control'}),
            'dni': TextInput(attrs={'class':'form-control'}),
            'telefono': TextInput(attrs={'class':'form-control'}),
            'mobil': TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': TextInput(attrs={'class':'form-control'}),
            'direccion': TextInput(attrs={'class':'form-control'}),
            'email': TextInput(attrs={'class':'form-control'}),
        }
 
class ProgramacionForm(ModelForm):
    class Meta:
        model = Programacion

    def __unicode__(self):
        return str(self.fecha)
'''
class form_user(forms.Form):
    user        = forms.CharField(max_length='15')  
    password    = forms.CharField(max_length=128, widget=forms.PasswordInput)
    active      = forms.BooleanField()
    fistname    = forms.CharField(max_length=200)
    lastname    = forms.CharField(max_length=200)
    dni         = forms.CharField(max_length=8)
    email       = forms.EmailField()
    group       = forms.ModelChoiceField(queryset=Group.objects.all())

    contrato_ingreso    = forms.CharField(widget=MyDateInput())
    contrato_salida     = forms.CharField(widget=MyDateInput())
    telefono            = forms.CharField(max_length=20,widget=MyTelephoneInput())
    direccion           = forms.CharField(max_length=200)
'''

class form_user(ModelForm):
    class Meta:
        model=User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'groups', 
            'is_active', 
        )

    username        = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name      = forms.CharField(label='Nombres',widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name       = forms.CharField(label='Apellidos',widget=forms.TextInput(attrs={'class':'form-control'}))
    email           = forms.EmailField(label='E-Mail',widget=forms.TextInput(attrs={'class':'form-control'}))
    password        = forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    groups          = forms.ModelMultipleChoiceField(queryset=Group.objects.all(),label='Grupo',widget=forms.SelectMultiple(attrs={'class':'form-control'}))
    is_active       = forms.BooleanField(label='Activo',widget=forms.CheckboxInput(attrs={'class':'form-control'}))

    form_name      = forms.CharField(widget=forms.HiddenInput(attrs={'class':'form-control', 'value':'usuario'}))


class form_perfil(ModelForm):
    class meta:
        model=Perfil
        fields=(
            'contrato_ingreso',
            'contrato_salida' ,
            'telefono',
            'dni',
            'direccion',
            )


class form_clinica(ModelForm):
    class Meta:
        model=Clinica
    nombre        = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'class':'form-control'}))
    direccion     = forms.CharField(label='Direccion',widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono      = forms.CharField(label='Telefono',widget=forms.TextInput(attrs={'class':'form-control'}))
    email         = forms.CharField(label='E-mail',widget=MyEmailInput(attrs={'class':'form-control'}))
    form_name      = forms.CharField(widget=forms.HiddenInput(attrs={ 'value':'clinica'}))


class form_escuela(ModelForm):
    class Meta:
        model=Escuela
    nombre        = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'class':'form-control'}))
    direccion     = forms.CharField(label='Direccion',widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono      = forms.CharField(label='Telefono',widget=forms.TextInput(attrs={'class':'form-control'}))
    email         = forms.CharField(label='E-mail',widget=MyEmailInput(attrs={'class':'form-control'}))
    form_name      = forms.CharField(widget=forms.HiddenInput(attrs={ 'value':'escuela'}))


class form_lugar(ModelForm):
    class Meta:
        model=Lugar

    nombres        = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'class':'form-control'}))
    direccion      = forms.CharField(label='Direccion',widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono       = forms.CharField(label='Telefono',widget=forms.TextInput(attrs={'class':'form-control'}))
    form_name      = forms.CharField(widget=forms.HiddenInput(attrs={ 'value':'lugar'}))

