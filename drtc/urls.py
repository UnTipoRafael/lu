from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drtc.views.home', name='home'),
    # url(r'^drtc/', include('drtc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),


	url(r'^$','examen.views.inicio',name="v_inicio"),
	url(r'^administrador$','examen.views.administrador'),
	url(r'^ingreso$','examen.views.ingreso'),
	url(r'^salir$','examen.views.salir',name='v_salir'),

	url(r'^registrador$','examen.views.registrador'),
	url(r'^evaluador$','examen.views.evaluador'),
	url(r'^busqueda$','examen.views.busqueda'),
	url(r'^info$','examen.views.info'),
	url(r'^evaluado$','examen.views.evaluado'),
	url(r'^ciudadano$','examen.views.ciudadano'),
	url(r'^programador$','examen.views.programador'),

	url(r'^info$','examen.views.info'),


	url(r'^examen$','examen.views.info'),


	url(r'^busca-dni/(?P<ndni>\d+)$','examen.views.busca_dni',name='busca_dni'),
	url(r'^programa-dni/(?P<ndni>\d+)$','examen.views.programa_dni',name='programa_dni'),


 	#url(r'^reprograma/(?P<ic>\d+)/(?P<f>\d+)/(?P<il>\d+)/(?P<t>\d+)/$','examen.views.reprograma_dni', name='reprograma'), 

)
