from django.urls import path
from . import views
from django.conf.urls import url
app_name = 'cal'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'index.html', views.index, name='index'),
    path(r'medical_appointment', views.medical_appointment, name='medical_appointment'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),


]