from django.test import SimpleTestCase
from django.utils import timezone
from django.shortcuts import render, redirect
from .models import ClientProfile, GradeMedic
from django.contrib.auth.models import User
from django.urls import reverse, resolve
## para probar views ##
from django.test import TestCase, Client
from .views import index, profile, register, get_grade_doctor
from .forms import ExtendedUserCreationForm, UserProfileForm, form_doctor_grade
from .models import ClientProfile, GradeMedic, User
import json

# Create your tests here.

## Pruebas para las urls
class Test(SimpleTestCase):
####################
### TEST VIEWS #####
####################
    def test_register_model_Get(self):
        cliente = Client()
        response = cliente.get(reverse('log:registro'))
        print(response)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'register.html')
    
    def test_index_model_Get(self):
        cliente = Client()
        response = cliente.get(reverse('log:calificacion'))
        self.assertEquals(response.status_code, 200)#redireccionado codigo        
        self.assertTemplateUsed(response, 'pet_care/user/calificacionM.html')

    def test_calificacion_model_Get(self):
        cliente = Client()
        response = cliente.get(reverse('log:calificacion'))        
        self.assertEquals(response.status_code, 200)#redireccionado codigo
        self.assertTemplateUsed(response, 'pet_care/user/calificacionM.html')

    def test_perfil_model_get(self):
        cliente = Client()
        response = cliente.get(reverse('log:perfil'))        
        self.assertEquals(response.status_code, 302)#redireccionado codigo 302



###################
### TEST Urls #####
###################
    def test_index_registro_is_resolved(self):
        url = reverse('log:registro')
        self.assertEquals(resolve(url).url_name,'registro')
    
    def test_index_perfil_is_resolved(self):
        url = reverse('log:perfil')
        self.assertEquals(resolve(url).url_name,'perfil')

    def test_index_logout_is_resolved(self):
        url = reverse('log:logout')
        self.assertEquals(resolve(url).url_name,'logout')
    
    def test_index_calificacion_is_resolved(self):
        url = reverse('log:calificacion')
        self.assertEquals(resolve(url).url_name,'calificacion')

    def test_index_login_is_resolved(self):
        url = reverse('log:login')
        self.assertEquals(resolve(url).url_name,'login')

####TEST URL CRUD CLIENTE
    def test_create_client_is_resolved(self):
        url = reverse('log:Create_client')
        self.assertEquals(resolve(url).url_name,'crear_cliente')
    def test_delete_client_is_resolved(self):
        url = reverse('log:Delete_client')
        self.assertEquals(resolve(url).url_name,'borrar_cliente')
    def test_modify_cliente_is_resolved(self):
        url = reverse('log:Modify_client')
        self.assertEquals(resolve(url).url_name,'modificar_cliente')

#####TEST VIEW CRUD CLIENTE
    def test_client_model_get(self):
        cliente = Client()
        response = cliente.get(reverse('log:Create_client'))
        self.assertEquals(response.status_code, 302)

