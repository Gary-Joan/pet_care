from django.test import SimpleTestCase
from app_pet_care.forms import *

class TestForms(SimpleTestCase):

    def test_login_administrator_form_valid_data(self):
        form = login_administrador(
            data={
                'user':'admin@admin.com',
                'password':'administrador'
            }
        )
        self.assertTrue(form.is_valid())

    def test_login_administrator_form_no_data(self):
        form = login_administrador(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),2)

    def test_new_veterinarian_form_valid_data(self):
        form = new_veterinarian_form(
            data={
                'name':'prueba',
                'telephone':'555454165',
                'mail':'prueba@prueba.com',
                'address':'Guatemala',
                'photo':'',
                'password':'44451',
                'birth_date':'29/4/1990',
                'dpi':'5456494855',
                'collected_number':'445551771'
            }
        )
        self.assertTrue(form.is_valid())

    def test_new_veterinarian_form_no_data(self):
        form = new_veterinarian_form(data={})
        self.assertFalse(form.is_valid())