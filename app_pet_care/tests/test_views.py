from django.test import TestCase, Client
from django.urls import reverse
from app_pet_care.models import *
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_administrator = reverse('cal:index_administrator')

    def test_view_index_administrator_resolved(self):
        response = self.client.get(self.index_administrator)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'pet_care/administrator/index.html')
