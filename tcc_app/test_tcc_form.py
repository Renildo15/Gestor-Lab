from django.test import TestCase
from tcc_app.forms import TccForm

class ProjetoFormTestCase(TestCase):

    def test_tcc_form_valido(self):
        form = TccForm(data={
            'Titulo':'TCC 01',
            'Autores': 1,
            'Orientadores': 1,
            'Instituicao': 'UFRN',
            'Descricao': 'teste',
            'Pesquisa': 1,
            
        })

        self.assertTrue(form.errors)

    def test_tcc_form_invalido(self):
        form = TccForm(data={})
        self.assertFalse(form.is_valid())