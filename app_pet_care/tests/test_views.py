from django.test import TestCase, Client
from django.urls import reverse
from app_pet_care.models import *
from app_pet_care.forms import *
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index = reverse('cal:index')
        self.index_client = reverse('cal:cliente')
        self.calendar = reverse('cal:calendar')
        self.event_new = reverse('cal:event_new')
        self.event_edit = reverse('cal:event_edit', args=[1])
        self.index_veterinarian = reverse('cal:index_veterinarian')
        self.home_veterinarian = reverse('cal:home_veterinarian')
        self.profile_veterinarian = reverse('cal:profile_veterinarian')
        self.logout_veterinarian = reverse('cal:logout_veterinarian')
        self.top10_dog_veterinarian = reverse('cal:top10_razas_perros_atendidos')
        self.index_administrator = reverse('cal:index_administrator')
        self.home_administrator = reverse('cal:home_administrator')
        self.logout_administrator = reverse('cal:logout_administrator')
        self.new_veterinarian_administrator = reverse('cal:new_veterinarian_administrator')
        self.update_veterinarian_administrator = reverse('cal:update_veterinarian')
        self.save_profile_veterinarian_administrator = reverse('cal:save_profile_veterinarian_administrator')
        self.delete_veterinarian_administrator = reverse('cal:delete_veterinarian')
        self.profile_administrator = reverse('cal:profile_administrator')
        self.new_administrator = reverse('cal:new_administrator')
        self.delete_administrator = reverse('cal:delete_administrator')

        Event.objects.create(
            title = 'candy',
            description='mal de estomago',
            start_time='2019-10-02 12:00:00'
        )

        self.veterinarian = Veterinarian.objects.create(
            dpi = 4445522115,
            name = 'test',
            photo = '20180826_163049.jpg',
            telephone = '12345678',
            mail = 'test@test.com',
            address = 'Guatemala',
            birth_date = '1993-12-01',
            collected_number = 123455524,
            password = 'test1234'
        )

        self.administrator = Administrator.objects.create(
            name = 'administrator test',
            password = 'test1234',
            dpi = 5416516315185,
            telephone = '45698788',
            mail = 'admin@admin.com',
            address = 'Guatemala'
        )

        self.admin2 = Administrator.objects.create(
            name = 'administrator test 2',
            password = 'test1234',
            dpi = 561777886315185,
            telephone = '45698788',
            mail = 'admin2@admin.com',
            address = 'Guatemala'
        )

    def test_view_index_resolved(self):
        response = self.client.get(self.index)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'pet_care/standard_pages/index.html')

    def test_view_index_client_resolved(self):
        response = self.client.get(self.index_client)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'pet_care/user/cliente.html')

    def test_view_calendar_resolved(self):
        response = self.client.get(self.calendar)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'cal/calendar.html')

    def test_view_event_new_resolved(self):
        response = self.client.get(self.event_new)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'cal/event.html')

    def test_view_event_edit_resolved(self):
        response = self.client.get(self.event_edit)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'cal/event.html')

    def test_view_index_veterinarian_resolved(self):
        response = self.client.get(self.index_veterinarian)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'pet_care/veterinarian/index.html')

    def test_view_home_veterinarian_no_data_resolved(self):
        response = self.client.get(self.home_veterinarian)
        self.assertEqual(response.status_code,302)

    def test_view_profile_veterinarian_no_data_resolved(self):
        response = self.client.get(self.profile_veterinarian)
        self.assertEqual(response.status_code,302)

    def test_view_logout_veterinarian_no_data_resolved(self):
        response = self.client.get(self.logout_veterinarian)
        self.assertEqual(response.status_code,302)

    def test_view_top10_dog_breedes_veterinarian_no_data_resolved(self):
        response = self.client.get(self.top10_dog_veterinarian)
        self.assertEqual(response.status_code,302)

    def test_view_index_veterinarian_login_resolved(self):
        response = self.client.post(
            self.index_veterinarian,
            {'user':self.veterinarian.mail,'password':self.veterinarian.password})
        self.assertEqual(response.status_code,302)

    def test_view_veterinarian_login_home_resolved(self):
        response = self.client.post(
            self.index_veterinarian,
            {'user':self.veterinarian.mail,'password':self.veterinarian.password})
        self.assertEqual(response.status_code,302)

        response = self.client.get(self.home_veterinarian,{'id_veterinarian':self.veterinarian.id})
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'pet_care/veterinarian/home.html')

    def test_view_veterinarian_login_profile_resolved(self):
        response = self.client.post(
            self.index_veterinarian,
            {'user':self.veterinarian.mail,'password':self.veterinarian.password})
        self.assertEqual(response.status_code,302)

        response = self.client.get(self.profile_veterinarian,{'id_veterinarian':self.veterinarian.id})
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'pet_care/veterinarian/profile.html')

    def test_view_veterinarian_login_profile_post_resolved(self):
        response = self.client.post(
            self.index_veterinarian,
            {'user':self.veterinarian.mail,'password':self.veterinarian.password})
        self.assertEqual(response.status_code,302)

        response = self.client.post(self.profile_veterinarian,
        {
            'id_veterinarian':self.veterinarian.id,
            'dpi':self.veterinarian.dpi,
            'name':self.veterinarian.name,
            'telephone': self.veterinarian.telephone,
            'mail':self.veterinarian.mail,
            'address':self.veterinarian.address,
            'collected_number':self.veterinarian.collected_number,
            'birth_date':self.veterinarian.birth_date
        })
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'pet_care/veterinarian/profile.html') 

    def test_view_veterinarian_top10_login_resolved(self):
        response = self.client.post(
            self.index_veterinarian,
            {'user':self.veterinarian.mail,'password':self.veterinarian.password})
        self.assertEqual(response.status_code,302)

        response = self.client.get(self.top10_dog_veterinarian,{'id_veterinarian':self.veterinarian.id})
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'pet_care/veterinarian/top10_dog_breeds.html')

    def test_view_veterinarian_logout_login_resolved(self):
        response = self.client.post(
            self.index_veterinarian,
            {'user':self.veterinarian.mail,'password':self.veterinarian.password})
        self.assertEqual(response.status_code,302)

        response = self.client.get(self.logout_veterinarian,{'id_veterinarian':self.veterinarian.id})
        self.assertEqual(response.status_code,302)

    def test_view_index_administrator_resolved(self):
        response = self.client.get(self.index_administrator)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'pet_care/administrator/index.html')
        
    def test_view_logout_administrator_no_data_resolved(self):
        response = self.client.get(self.logout_administrator)
        self.assertEqual(response.status_code,302)

    def test_view_home_administrator_no_data_resolved(self):
        response = self.client.get(self.home_administrator)
        self.assertEqual(response.status_code,302)

    def test_view_new_veterinarian_administrator_no_data_resolved(self):
        response = self.client.get(self.new_veterinarian_administrator)
        self.assertEqual(response.status_code,302)

    def test_view_update_veterinarian_administrator_no_data_resolved(self):
        response = self.client.get(self.update_veterinarian_administrator)
        self.assertEqual(response.status_code,302)

    def test_view_save_profile_veterinarian_administrator_no_data_resolved(self):
        response = self.client.get(self.save_profile_veterinarian_administrator)
        self.assertEqual(response.status_code,302)

    def test_view_delete_veterinarian_administrator_no_data_resolved(self):
        response = self.client.get(self.delete_veterinarian_administrator)
        self.assertEqual(response.status_code,302)

    def test_profile_administrator_no_data_resolved(self):
        response = self.client.get(self.profile_administrator)
        self.assertEqual(response.status_code,302)

    def test_new_administrator_administrator_no_data_resolved(self):
        response = self.client.get(self.new_administrator)
        self.assertEqual(response.status_code,302)

    def test_delete_administrator_administrator_no_data_resolved(self):
        response = self.client.get(self.delete_administrator)
        self.assertEqual(response.status_code,302)

    def test_administrator_login_resolved(self):
        response = self.client.post(self.index_administrator,
        {'user':self.administrator.mail,'password':self.administrator.password})
        self.assertEqual(response.status_code,302)

    def test_view_administrator_login_home_resolved(self):
        response = self.client.post(self.index_administrator,
        {'user':self.administrator.mail,'password':self.administrator.password})
        self.assertEqual(response.status_code,302)

        response = self.client.get(self.home_administrator,{'id_administrator':self.administrator.id})
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'pet_care/administrator/home.html')

    def test_view_administrator_login_profile_resolved(self):
        response = self.client.post(self.index_administrator,
        {'user':self.administrator.mail,'password':self.administrator.password})
        self.assertEqual(response.status_code,302)

        response = self.client.get(self.profile_administrator,{'id_administrator':self.administrator.id})
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'pet_care/administrator/profile_administrator.html')
    
    def test_view_administrator_login_profile_post_resolved(self):
        response = self.client.post(self.index_administrator,
        {'user':self.administrator.mail,'password':self.administrator.password})
        self.assertEqual(response.status_code,302)

        response = self.client.post(self.profile_administrator,
        {
            'id_administrator':self.administrator.id,
            'dpi': self.administrator.dpi,
            'name':self.administrator.name,
            'telephone':self.administrator.telephone,
            'mail': self.administrator.mail,
            'address':self.administrator.address
        })
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'pet_care/administrator/profile_administrator.html')

    def test_view_administrator_login_new_veterinarian_resolved(self):
        response = self.client.post(self.index_administrator,
        {'user':self.administrator.mail,'password':self.administrator.password})
        self.assertEqual(response.status_code,302)

        reponse = self.client.get(self.new_veterinarian_administrator,{'id_administrator':self.administrator.id})
        self.assertEqual(response.status_code,302)

    def test_view_administrator_login_new_veterinarian_post_resolved(self):
        response = self.client.post(self.index_administrator,
        {'user':self.administrator.mail,'password':self.administrator.password})
        self.assertEqual(response.status_code,302)

        response = self.client.post(self.new_veterinarian_administrator,
        {
            'id_administrator':self.administrator.id,
            'name':'veterinario',
            'dpi':2164165163,
            'telephone':'161561',
            'mail':'veterinario@veterinaria.com',
            'address':'Guatemala',
            'collected_number':545665156156,
            'photo':'20180826_163049.jpg',
            'birth_date':'2000/11/02',
            'password':'test1234'
        })
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'pet_care/administrator/home.html')

    def test_view_administrator_login_update_resolved(self):
        response = self.client.post(self.index_administrator,
        {'user':self.administrator.mail,'password':self.administrator.password})
        self.assertEqual(response.status_code,302)

        response = self.client.get(self.update_veterinarian_administrator,{'id_administrator':self.administrator.id})
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'pet_care/administrator/update_veterinarian.html')

    def test_view_administrator_login_update_post_resolved(self):
        response = self.client.post(self.index_administrator,
        {'user':self.administrator.mail,'password':self.administrator.password})
        self.assertEqual(response.status_code,302)

        response = self.client.get(self.update_veterinarian_administrator,
        {
            'id_administrator':self.administrator.id,
            'user_value':self.veterinarian.id
        })
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'pet_care/administrator/update_veterinarian.html')

    def test_view_administrator_login_save_profile_resolved(self):
        response = self.client.post(self.index_administrator,
        {'user':self.administrator.mail,'password':self.administrator.password})
        self.assertEqual(response.status_code,302)

        response = self.client.post(self.save_profile_veterinarian_administrator,
        {
            'id_administrator':self.administrator.id,
            'name':self.veterinarian.name,
            'dpi':self.veterinarian.dpi,
            'telephone':self.veterinarian.telephone,
            'mail':self.veterinarian.mail,
            'address':self.veterinarian.address,
        })
        self.assertEqual(response.status_code,302)
        
    def test_view_administrator_login_delete_resolved(self):
        response = self.client.post(self.index_administrator,
        {'user':self.administrator.mail,'password':self.administrator.password})
        self.assertEqual(response.status_code,302)

        response = self.client.get(self.delete_veterinarian_administrator,{'id_administrator':self.administrator.id})
        self.assertEqual(response.status_code,200)

    def tet_view_administrator_login_delete_post_resolved(self):
        response = self.client.post(self.index_administrator,
        {'user':self.administrator.mail,'password':self.administrator.password})
        self.assertEqual(response.status_code,302)

        response = self.client.post(self.delete_veterinarian_administrator,
        {
            'id_administrator':self.administrator.id,
            'user_value':self.veterinarian.id
        })
        self.assertEqual(reponse.status_code,200)
        self.assertTemplateUsed(response,'pet_care/administrator/delete_veterinarian.html')

    def test_view_administrator_login_new_administrator_resolved(self):
        response = self.client.post(self.index_administrator,
        {'user':self.administrator.mail,'password':self.administrator.password})
        self.assertEqual(response.status_code,302)

        response = self.client.get(self.new_administrator,{'id_administrator':self.administrator.id})
        self.assertEqual(response.status_code,200)

    def test_view_administrator_login_new_administrator_post_resolved(self):
        response = self.client.post(self.index_administrator,
        {'user':self.administrator.mail,'password':self.administrator.password})
        self.assertEqual(response.status_code,302)

        response = self.client.post(self.new_administrator,
        {
            'id_administrator':self.administrator.id,
            'dpi':654654145,
            'name':'nuevo admin',
            'telephone':'5645641456',
            'mail':'nuevo@admin.com',
            'address':'Guatemala',
            'password':'admin1234'
        })
        self.assertEqual(response.status_code,200)

    def test_view_administrator_login_delete_administrator_resolved(self):
        response = self.client.post(self.index_administrator,
        {'user':self.administrator.mail,'password':self.administrator.password})
        self.assertEqual(response.status_code,302)

        reponse= self.client.get(self.delete_administrator,{'id_administrator':self.administrator.id})
        self.assertEqual(reponse.status_code,200)

    def test_view_administrator_login_delete_administrator_post_resolved(self):
        response = self.client.post(self.index_administrator,
        {'user':self.administrator.mail,'password':self.administrator.password})
        self.assertEqual(response.status_code,302)

        response = self.client.post(self.delete_administrator,
        {
            'id_administrator':self.administrator.id,
            'user_value': self.admin2.id
        })
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'pet_care/administrator/delete_administrator.html')

    def test_view_administrator_login_logout_administrator_resolved(self):
        response = self.client.post(self.index_administrator,
        {'user':self.administrator.mail,'password':self.administrator.password})
        self.assertEqual(response.status_code,302)

        reponse = self.client.get(self.logout_administrator,{'id_administrator':self.administrator.id})
        self.assertEqual(reponse.status_code,302)