from django import forms

from django.contrib.auth.models import User, Group
from django.forms import ModelForm 
from examen.models import Ciudadano ,Programacion
from django.forms.widgets import TextInput, DateInput, DateTimeInput, TimeInput
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
