from django.test import TestCase
from apresentacao_app.forms import ApresentacaoForm

class ApresentacaoFormTestCase(TestCase):

    def test_apresentacao_form_valido(self):
        form = ApresentacaoForm(data={
            'Titulo':'Apresentação 01',
            'Autores': 1,
            'descricao': 1,
            'Projeto': 1
        })

        self.assertTrue(form.errors)

    def test_apresentacao_form_invalido(self):
        form = ApresentacaoForm(data={})
        self.assertFalse(form.is_valid())