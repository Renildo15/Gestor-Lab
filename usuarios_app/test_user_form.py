from django.test import TestCase
from usuarios_app.forms import RegisterUserForm, PasswordChangingForm

class UsuarioFormTestCase(TestCase):

    def test_user_form_valido(self):
        form = RegisterUserForm(data={
            'username':'Habby_Valle',
            'first_name': 'Renildo Rabi',
            'last_name': 'Vale Dos Santos',
            'email': 'habby@gmail.com',
            'password1': '12345678',
            'password2': '12345678',
            
        })

        self.assertTrue(form.errors)

    def test_user_form_invalido(self):
        form = RegisterUserForm(data={})
        self.assertFalse(form.is_valid())
