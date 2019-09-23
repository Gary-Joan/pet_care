from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cal'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cliente/$', views.indexCliente, name='cliente'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    
    #VETERINARIAN
    url(r'^veterinario/$',views.index_veterinarian, name='index_veterinarian'),
    url(r'^veterinario/inicio/$',views.home_veterinarian, name='home_veterinarian'),
    url(r'^veterinario/perfil/$', views.profile_veterinarian, name='profile_veterinarian'),
    url(r'^logout/$',views.logout_veterinarian,name='logout_veterinarian'),
    url(r'^veterinario/top10_razas_de_perros',views.top10_dog_breeds,name='top10_razas_perros_atendidos'),


    #ADMINISTRATOR
    url(r'^administrador$',views.index_administrator,name='index_administrator'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)