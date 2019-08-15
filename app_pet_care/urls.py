from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cal'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'index.html', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    
    #VETERINARIAN
    url(r'^veterinarian/$',views.index_veterinarian, name='index_veterinarian'),
    url(r'^veterinarian/home/$',views.home_veterinarian, name='home_veterinarian'),
    url(r'^vererinarian/home/perfil/$', views.profile_veterinarian, name='profile_veterinarian'),
    url(r'^logout/$',views.logout_veterinarian,name='logout_veterinarian'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)