from django.test import TestCase
from laboratorio_app.forms import LabForm

class LabFormTestCase(TestCase):

    def test_lab_form_valido(self):
        form = LabForm(data={
            'Nome':'Laboratorio 01',
            'Sigla': 'Lab01',
            'Coordenador': 'Habby',
            'Vice_coordenador': 'Renildo'
        })

        self.assertTrue(form.errors)

    def test_lab_form_invalido(self):
        form = LabForm(data={})
        self.assertFalse(form.is_valid())