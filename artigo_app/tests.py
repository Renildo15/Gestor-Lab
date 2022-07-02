import email
from django.test import TestCase
from artigo_app.models import Artigo
from laboratorio_app.models import Lab
from membros_app.models import Membro

class Artigo_Teste(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Artigo.objects.create(titulo='Programação orientada a Objetos', local_Publi = 'Jardim do Seridó', descricao = 'Artigo relacionado a Programação OO')

    # Teste do Att titulo #
    def teste_titulo_label(self):
        art = Artigo.objects.get(id=1)
        field_label = art._meta.get_field('titulo').verbose_name
        self.assertEquals(field_label, 'titulo')
    def teste_titulo_tamanho(self):
        art = Artigo.objects.get(id=1)
        max_length = art._meta.get_field('titulo').max_length
        self.assertEquals(max_length, 50)

    # Teste do Att local_Publi #

    def teste_local_Publi_label(self):
        art = Artigo.objects.get(id=1)
        field_label = art._meta.get_field('local_Publi').verbose_name
        self.assertEquals(field_label, 'local_Publi')
    def teste_local_Publi_tamanho(self):
        art = Artigo.objects.get(id=1)
        max_length = art._meta.get_field('local_Publi').max_length
        self.assertEquals(max_length, 200)

    # teste do Att descricao #

    def teste_descricao_label(self):
        art = Artigo.objects.get(id=1)
        field_label = art._meta.get_field('descricao').verbose_name
        self.assertEquals(field_label, 'descricao')
    def teste_descricao_tamanho(self):
        art = Artigo.objects.get(id=1)
        max_length = art._meta.get_field('descricao').max_length
        self.assertEquals(max_length, 200)
    # Teste do Att autores #

class AutoresTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Membro.objects.create(nome = 'Jeison')
    
    def teste_nomeautor_label(self):
        membro = Membro.objects.get(id=1)
        field_label = membro._meta.get_field('nome').verbose_name
        self.assertEquals(field_label, 'nome')
    def testnomeautorTamanho(self):
        membro = Membro.objects.get(id=1)
        max_length = membro._meta.get_field('nome').max_length
        self.assertEquals(max_length, 60)

        # Teste do Att laboratorio_art #

class LaboratorioTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Lab.objects.create(nome = 'DCT')
    
    def teste_nomelab_label(self):
        laboratorio = Lab.objects.get(id=1)
        field_label = laboratorio._meta.get_field('nome').verbose_name
        self.assertEquals(field_label, 'nome')
