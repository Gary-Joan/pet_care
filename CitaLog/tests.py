from django.test import TestCase
from django.utils import timezone

from .models import EventCita
# Create your tests here.

#Prueba para lista de mascotas
def test_ListaMascotas_is_resolved(self):
        url = reverse('log:ListaMascotas')
        self.assertEquals(resolve(url).url_name,'ListaMascotas')
