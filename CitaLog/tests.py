from django.test import TestCase
from django.utils import timezone
from django.urls import reverse, resolve

from .models import EventCita
# Create your tests here.

#Prueba para lista de mascotas
def test_ListaMascotas_is_resolved(self):
    url = reverse('cita:ListaMascotas')
    self.assertEquals(resolve(url).url_name,'ListaMascotas')

def test_BorrarMascotasConfirmacion_is_resolved(self):
    url = reverse('cita:BorrarMascotasConfirmacion')
    self.assertEquals(resolve(url).url_name,'BorrarMascotasConfirmacion')

def test_BorrarMascotas_is_resolved(self):
    url = reverse('cita:BorrarMascota')
    self.assertEquals(resolve(url).url_name,'ListaMascotas')

def test_GenerarPDFInfoCita_is_resolved(self):
    url = reverse('cita:GenerarPDFInfoCita')
    self.assertEquals(resolve(url).url_name,'GenerarPDFInfoCita')


#pruebas para CRUD servicios

def test_CreateServices_is_resolved(self):
    url = reverse('cita:CrearServicio')
    self.assertEquals(resolve(url).url_name,'CrearServicio')

def test_ListServices_is_resolved(self):
    url = reverse('cita:ListaServicio')
    self.assertEquals(resolve(url).url_name,'ListaServicios')

def test_deleteServices_is_resolved(self):
    url = reverse('cita:BorrarServicio')
    self.assertEquals(resolve(url).url_name,'BorrarServicio')