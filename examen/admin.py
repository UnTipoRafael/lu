from django.contrib import admin

from examen.models import Lugar
from examen.models import Escuela
from examen.models import Clinica

from examen.models import Perfil
from examen.models import Ciudadano
from examen.models import Registro

from examen.models import Programacion
from examen.models import Preguntas
from examen.models import Respuestas

from examen.models import Examen


admin.site.register(Lugar)
admin.site.register(Escuela)
admin.site.register(Clinica)
admin.site.register(Perfil)
admin.site.register(Ciudadano)
admin.site.register(Registro)
admin.site.register(Programacion)
admin.site.register(Preguntas)
admin.site.register(Respuestas)
admin.site.register(Examen)


