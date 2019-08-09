from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/medical_appointment', views.medical_appointment,name='medical_appointment'),
]