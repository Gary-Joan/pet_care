from django.test import SimpleTestCase
from app_pet_care.forms import *

class TestForms(SimpleTestCase):

    def test_login_administrator_form_valid_data(self):
        form = login_administrador(
            data={
                'user':'administrador',
                'password':'administrador'
            }
        )
        self.assertTrue(form.is_valid())

    def test_login_administrator_form_no_data(self):
        form = login_administrador(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),2)