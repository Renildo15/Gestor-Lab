from django.test import TestCase
from laboratorio_app.models import Lab

# Create your tests here.


class LabTest(TestCase):
    # teste campo nome
    @classmethod
    def setUpTestData(cls):
        Lab.objects.create(nome='Lab 01', sigla='LAB',descricao='teste')


    def testNameLabeling(self):
        lab = Lab.objects.get(id=1)
        field_label = lab._meta.get_field('nome').verbose_name
        self.assertEquals(field_label, 'nome')

    def testNameLength(self):
        lab = Lab.objects.get(id=1)
        max_length = lab._meta.get_field('nome').max_length
        self.assertEquals(max_length,60)

    # teste campo sigla

    def testSiglaLabeling(self):
        lab = Lab.objects.get(id=1)
        field_label = lab._meta.get_field('sigla').verbose_name
        self.assertEquals(field_label, 'sigla')

    def testSiglaLength(self):
        lab = Lab.objects.get(id=1)
        max_length = lab._meta.get_field('sigla').max_length
        self.assertEquals(max_length,25)


    # teste campo descricao

    def testDescricaoLabeling(self):
        lab = Lab.objects.get(id=1)
        field_label = lab._meta.get_field('descricao').verbose_name
        self.assertEquals(field_label, 'descricao')

    def testDescricaoLength(self):
        lab = Lab.objects.get(id=1)
        max_length = lab._meta.get_field('descricao').max_length
        self.assertEquals(max_length,200)