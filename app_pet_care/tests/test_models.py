
from app_pet_care.models import Event, Administrator

from django.test import TestCase

class LoginModelTest(TestCase):

    def test_event_creation(self):
        Event(title = "max", description="prueba de description", start_time="2019-09-01").save()
        events = Event.objects.all()
        eventos = Event.objects.get(id=1)
        self.assertEquals(events.count(), 1)
        self.assertEquals(eventos.title, "max")

    def test_user_administrator(self):
        Administrator(
            name = "administrador",
            password = "1234",
            dpi = 1234567891011,
            telephone = "12345678",
            mail = "admin@admin.com",
            address = "Guatemala",
        ).save()
        administradores = Administrator.objects.all()
        administrador = Administrator.objects.get(id=1)
        self.assertEquals(administradores.count(),1)
        self.assertEquals(administrador.name,"administrador")