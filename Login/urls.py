from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'log'
urlpatterns = [

    url(r'^registro/$', views.register, name='registro'),
    url(r'^perfil/$', views.index, name='perfil'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^calificacion/$', views.get_grade_doctor, name='calificacion'),
    url(r'^Top3Medicos/$', views.Top3BestDoctor, name='topdoctor'),

    url(r'^$', LoginView.as_view(template_name='login.html'), name="login"),
]


