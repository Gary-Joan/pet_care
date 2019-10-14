from django.conf.urls import url
from . import views

app_name = 'cita'
urlpatterns = [
    url(r'^$', views.index, name='indexC'),
    url(r'^calendarC/$', views.CalendarView.as_view(), name='calendarC'),
    url(r'^eventC/newC/$', views.event, name='event_newC'),
    url(r'^eventC/editC/(?P<event_id>\d+)/$', views.event, name='event_editC'),
    url(r'^Historial/Mascota/(?P<NombreMascota>.+)$', views.HistorialPorMascota, name = 'HistorialPorMascota'),
    url(r'^Historial/Cliente/(?P<NombreCliente>.+)$', views.HistorialPorCliente, name = 'HistorialPorCliente'),
    url(r'^Historial/$', views.Historial, name='Historial'),
    url(r'^ListaMascotas/$', views.ListaMascotas, name='ListaMascotas'),
    url(r'^ConfirmacionBorrarMascota/(?P<NombreCliente>.+)/(?P<NombreMascota>.+)$', views.ConfirmacionBorrarMascota, name='ConfirmacionBorrarMascota'),
    url(r'^BorrarDatoMascota/(?P<NombreCliente>.+)/(?P<NombreMascota>.+)/(?P<Fecha>.+)/(?P<Hora>.+)$', views.BorrarMascota, name='BorrarMascota'),
    url(r'^GenerarPDFInfoCita/(?P<NombreCliente>.+)/(?P<NombreMascota>.+)/(?P<Fecha>.+)/(?P<Hora>.+)$', views.GenerarPDFInfoCita, name='GenerarPDFInfoCita'),
    #url(r'^AgregarUtensilio/$', views.CrearUtensilio, name='CrearUtensilio'),
    url(r'^ListarUtensilios/$', views.ListaUtensilios, name='ListaUtensilios'),
    url(r'^BorrarUtensilio/(?P<id>\d+)/$', views.BorrarUtensilio, name='BorrarUtensilio')
]
