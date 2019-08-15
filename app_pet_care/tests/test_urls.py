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