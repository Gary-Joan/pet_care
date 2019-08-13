from django.conf.urls import url
from . import views

app_name = 'cita'
urlpatterns = [
    url(r'^$', views.event, name='indexC'),
    url(r'^calendarC/$', views.CalendarView.as_view(), name='calendarC'),
    url(r'^eventC/newC/$', views.event, name='event_newC'),
	url(r'^eventC/editC/(?P<event_id>\d+)/$', views.event, name='event_editC'),
]
