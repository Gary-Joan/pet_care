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

def test_CreateUtensilio_is_resolved(self):
    url = reverse('cita:CrearUtensilio')
    self.assertEquals(resolve(url).url_name,'CrearUtensilio')

def test_ListUtensilio_is_resolved(self):
    url = reverse('cita:ListaUtensilios')
    self.assertEquals(resolve(url).url_name,'ListaUtensilios')

def test_BorrarUtensilio_is_resolved(self):
    url = reverse('cita:BorrarUtensilio')
    self.assertEquals(resolve(url).url_name,'BorrarUtensilio')


#pruebas para CRUD servicios

