from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from linhapesquisa_app.models import LinhaPesquisa

class LinhaPesquisaTeste(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        LinhaPesquisa.objects.create(nome='Jogos na educação', descricao='Análise do uso de jogos na educação', areaCNPQ = 'Computação', subAreaCNPQ = 'jogos')

    def teste_nome_label(self):
        pesquisa = LinhaPesquisa.objects.get(id=1)
        field_label = pesquisa._meta.get_field('nome').verbose_name
        self.assertEquals(field_label, 'nome')

    def teste_descricao_label(self):
        pesquisa = LinhaPesquisa.objects.get(id=1)
        field_label = pesquisa._meta.get_field('descricao').verbose_name
        self.assertEquals(field_label, 'descricao')

    def teste_areaCNPQ_label(self):
        pesquisa = LinhaPesquisa.objects.get(id=1)
        field_label = pesquisa._meta.get_field('areaCNPQ').verbose_name
        self.assertEquals(field_label, 'areaCNPQ')
    
    def teste_subAreaCNPQ_label(self):
        pesquisa = LinhaPesquisa.objects.get(id=1)
        field_label = pesquisa._meta.get_field('subAreaCNPQ').verbose_name
        self.assertEquals(field_label, 'subAreaCNPQ')

    def teste_nome_tamanho(self):
        pesquisa = LinhaPesquisa.objects.get(id=1)
        max_length = pesquisa._meta.get_field('nome').max_length
        self.assertEquals(max_length, 60)

    def teste_descricao_tamanho(self):
        pesquisa = LinhaPesquisa.objects.get(id=1)
        max_length = pesquisa._meta.get_field('descricao').max_length
        self.assertEquals(max_length, 200)
    
    def teste_areaCNPQ_tamanho(self):
        pesquisa = LinhaPesquisa.objects.get(id=1)
        max_length = pesquisa._meta.get_field('areaCNPQ').max_length
        self.assertEquals(max_length, 150)
    
    def teste_subAreaCNPQ_tamanho(self):
        pesquisa = LinhaPesquisa.objects.get(id=1)
        max_length = pesquisa._meta.get_field('subAreaCNPQ').max_length
        self.assertEquals(max_length, 150)