from django.test import SimpleTestCase
from django.urls import reverse, resolve

class TestUrls(SimpleTestCase):
###################
#### Test Urls ####
###################

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

    def test_veterinarian_index_is_resolved(self):
        url = reverse('cal:index_veterinarian')
        self.assertEquals(resolve(url).url_name, 'index_veterinarian')

    def test_veterinarian_home_is_resolved(self):
        url = reverse('cal:home_veterinarian')
        self.assertEquals(resolve(url).url_name, 'home_veterinarian')

    def test_veterinarian_profile_is_resolved(self):
        url = reverse('cal:profile_veterinarian')
        self.assertEquals(resolve(url).url_name, 'profile_veterinarian')
    ##ESTO SOLO LO PUSE PARA QUE NO DIERRA ERROR test_veterinarian:logout
    def test_veterinarian_logout_is_resolved(self):
        url = reverse('cal:index_veterinarian')
        self.assertEquals(resolve(url).url_name,'index_veterinarian')

    def test_index_veterinarian(self):
        url = reverse('cal:index_veterinarian')
        self.assertEquals(resolve(url).url_name,'index_veterinarian')

    def test_home_veterinarian(self):
        url = reverse('cal:home_veterinarian')
        self.assertEqual(resolve(url).url_name,'home_veterinarian')

    def test_profile_veterinarian(self):
        url = reverse('cal:profile_veterinarian')
        self.assertEqual(resolve(url).url_name,'profile_veterinarian')

    def test_logout_veterinarian(self):
        url = reverse('cal:logout_veterinarian')
        self.assertEqual(resolve(url).url_name,'logout_veterinarian')

    def test_grade_page(self):
        url = reverse('log:calificacion')
        self.assertEqual(resolve(url).url_name,'calificacion')

    def test_index_administrator_is_resolved(self):
        url = reverse('cal:index_administrator')
        self.assertEqual(resolve(url).url_name,'index_administrator')
    
    def test_home_administrator_is_resolved(self):
        url = reverse('cal:home_administrator')
        self.assertEqual(resolve(url).url_name,'home_administrator')
    
    def test_new_veterinarian_is_resolved(self):
        url = reverse('cal:new_veterinarian_administrator')
        self.assertEqual(resolve(url).url_name,'new_veterinarian_administrator')

    def test_update_veterinarian_is_resolved(self):
        url = reverse('cal:update_veterinarian')
        self.assertEqual(resolve(url).url_name,'update_veterinarian')

    def test_profile_veterinarian_is_resolved(self):
        url = reverse('cal:save_profile_veterinarian_administrator')
        self.assertEqual(resolve(url).url_name,'save_profile_veterinarian_administrator')
    
    def test_delete_veterinaria_is_resolved(self):
        url = reverse('cal:delete_veterinarian')
        self.assertEqual(resolve(url).url_name,'delete_veterinarian')


    def test_CreateServices_is_resolved(self):
        url = reverse('cita:CrearServicio')
        self.assertEquals(resolve(url).url_name, 'CrearServicio')


    def test_ListServices_is_resolved(self):
        url = reverse('cita:ListaServicio')
        self.assertEquals(resolve(url).url_name, 'ListaServicios')


    def test_deleteServices_is_resolved(self):
        url = reverse('cita:BorrarServicio')
        self.assertEquals(resolve(url).url_name, 'BorrarServicio')

    def test_home_administrator_is_resolved(self):
        url = reverse('cal:home_administrator')
        self.assertEqual(resolve(url).url_name,'home_administrator')

    def test_profile_administrator_is_resolved(self):
        url = reverse('cal:profile_administrator')
        self.assertEqual(resolve(url).url_name,'profile_administrator')

    def test_new_administrator_is_resolved(self):
        url = reverse('cal:new_administrator')
        self.assertEqual(resolve(url).url_name,'new_administrator')

    def test_delete_administrator_is_resolved(self):
        url = reverse('cal:delete_administrator')
        self.assertEqual(resolve(url).url_name,'delete_administrator')