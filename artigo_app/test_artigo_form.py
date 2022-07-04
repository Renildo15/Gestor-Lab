from django.test import TestCase
from artigo_app.forms import ArtForm

class ArtFormTestCase(TestCase):

    def test_artigo_form_valido(self):
        form = ArtForm(data={
            'Título':'Artigo 01',
            'Autores': 1,
            'Local Da Publicação': 'https://github.com/Renildo15',
            'Descrição': 'teste',
            'Laboratório': 1
        })

        self.assertTrue(form.errors)

    def test_artigo_form_invalido(self):
        form = ArtForm(data={})
        self.assertFalse(form.is_valid())