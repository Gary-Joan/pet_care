from django.urls import path
from . import views
    url(r'^medical_appointment/$', views.medical_appointment, name='medical_appointment'),


]