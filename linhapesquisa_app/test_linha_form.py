from django.test import TestCase
from linhapesquisa_app.forms import LinhaForm

class LinhaFormTestCase(TestCase):

    def test_linha_form_valido(self):
        form = LinhaForm(data={
            'Nome':'Pesquisa 01',
            'Descrição': 'Teste',
            'Área': 'Teste',
            'CNPQ': 'Teste',
            'laboratório': 1,
        })

        self.assertTrue(form.errors)

    def test_linha_form_invalido(self):
        form = LinhaForm(data={})
        self.assertFalse(form.is_valid())