from django.test import TestCase
from artigo_app.models import Artigo

class Artigo_Teste(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Artigo.objects.create(titulo='Programação orientada a Objetos', local_Publi = 'Jardim do Seridó', descricao = 'Artigo relacionado a Programação OO')

    def teste_titulo_label(self):
        art = Artigo.objects.get(id=1)
        field_label = art._meta.get_field('titulo').verbose_name
        self.assertEquals(field_label, 'titulo')

    def teste_local_Publi_label(self):
        art = Artigo.objects.get(id=1)
        field_label = art._meta.get_field('local_Publi').verbose_name
        self.assertEquals(field_label, 'local_Publi')

    def teste_descricao_label(self):
        art = Artigo.objects.get(id=1)
        field_label = art._meta.get_field('descricao').verbose_name
        self.assertEquals(field_label, 'descricao')
    
    def teste_titulo_tamanho(self):
        art = Artigo.objects.get(id=1)
        max_length = art._meta.get_field('titulo').max_length
        self.assertEquals(max_length, 50)

    def teste_local_Publi_tamanho(self):
        art = Artigo.objects.get(id=1)
        max_length = art._meta.get_field('local_Publi').max_length
        self.assertEquals(max_length, 200)

    def teste_descricao_tamanho(self):
        art = Artigo.objects.get(id=1)
        max_length = art._meta.get_field('descricao').max_length
        self.assertEquals(max_length, 200)