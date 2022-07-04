from django.test import TestCase
from evento_app.forms import EventForm

class EventoFormTestCase(TestCase):

    def test_apresentar_form_valido(self):
        form = EventForm(data={
            'Nome':'Evento 01',
            'E-Mail': 'teste@gmail.com',
            'Telefone': '(84) 9 9999-9999',
            'Laboratório': 1,
            'Site': 'https://github.com/Renildo15',
            
        })

        self.assertTrue(form.errors)

    def test_pessoa_form_invalido(self):
        form = EventForm(data={})
        self.assertFalse(form.is_valid())