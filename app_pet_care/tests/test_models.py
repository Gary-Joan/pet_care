
from app_pet_care.models import Event

from django.test import TestCase

class LoginModelTest(TestCase):

    def test_event_creation(self):
        Event(title = "max", description="prueba de description", start_time="2019-09-01").save()
        events = Event.objects.all()
        eventos = Event.objects.get(id=1)
        self.assertEquals(events.count(), 1)
        self.assertEquals(eventos.title, "max")
