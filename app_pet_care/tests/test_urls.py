from django.test import SimpleTestCase
from django.urls import reverse, resolve



class TestUrls(SimpleTestCase):

    def test_index_cliente_is_resolved(self):
        url = reverse('cal:index')
        self.assertEquals(resolve(url).url_name, 'index')

    def test_cliente_is_resolved(self):
        url = reverse('cal:cliente')
        self.assertEquals(resolve(url).url_name, 'cliente')

    def test_calendar_is_resolved(self):
        url = reverse('cal:calendar')
        self.assertEquals(resolve(url).url_name, 'calendar')

    def test_new_event_is_resolved(self):
        url = reverse('cal:event_new')
        self.assertEquals(resolve(url).url_name, 'event_new')

    def test_index_veterinarian(self):
        url = reverse('cal:index_veterinarian')
        self.assertEquals(resolve(url).url_name,'index_veterinarian')

    def test_home_veterinarian(self):
        url = reverse('cal:home_veterinarian')
        self.assertEqual(resolve(url).url_name,'home_veterinarian')

    def test_profile_veterinarian(self):
        url = reverse('cal:profile_veterinarian')
        self.assertEquals(resolve(url).url_name,'profile_veterinarian')

    def test_logout_veterinarian(self):
        url = reverse('cal:logout_veterinarian')
        self.assertEquals(resolve(url).url_name,'logout_veterinarian')