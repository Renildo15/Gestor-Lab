from django.test import TestCase
from estagio_app.forms import EstForm

class EstagioFormTestCase(TestCase):

    def test_estagio_form_valido(self):
        form = EstForm(data={
            'Estagiario': 1,
            'Orientador': 2,
            'Supervisor': 3,
            'Atividade': 'Atividade 01',
            'Laboratório': 1
        })

        self.assertTrue(form.errors)

    def test_estagio_form_invalido(self):
        form = EstForm(data={})
        self.assertFalse(form.is_valid())