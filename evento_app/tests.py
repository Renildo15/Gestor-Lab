from django.test import TestCase
from evento_app.models import Evento

# Create your tests here.


    

class EventoTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Evento.objects.create(titulo='evento01', area='teste', laboratorio='1', site='teste.com', descricao='testes dos testes')

    # teste campo nome
    def testNameLabeling(self):
        event = Evento.objects.get(id=1)
        field_label = event._meta.get_field('titulo').verbose_name
        self.assertEquals(field_label, 'titulo')

    def testNameLength(self):
        event = Evento.objects.get(id=1)
        max_length = event._meta.get_field('titulo').max_length
        self.assertEquals(max_length,50)

    # teste campo area

    def testAreaLabeling(self):
        event = Evento.objects.get(id=1)
        field_label = event._meta.get_field('area').verbose_name
        self.assertEquals(field_label, 'area')

    def testAreaLength(self):
        event = Evento.objects.get(id=1)
        max_length = event._meta.get_field('area').max_length
        self.assertEquals(max_length,50)


    # teste campo laboratorio

    def testLaboratorioLabeling(self):
        event = Evento.objects.get(id=1)
        field_label = event._meta.get_field('laboratorio').verbose_name
        self.assertEquals(field_label, 'laboratorio')

    # teste do campo site

    def testSiteLabeling(self):
        event = Evento.objects.get(id=1)
        field_label = event._meta.get_field('site').verbose_name
        self.assertEquals(field_label, 'site')

    def testSiteLength(self):
        event = Evento.objects.get(id=1)
        max_length = event._meta.get_field('site').max_length
        self.assertEquals(max_length,200)

    # teste do campo descricao

    def testDescricaoLabeling(self):
        event = Evento.objects.get(id=1)
        field_label = event._meta.get_field('descricao').verbose_name
        self.assertEquals(field_label, 'descricao')

    def testDescricaoLength(self):
        event = Evento.objects.get(id=1)
        max_length = event._meta.get_field('descricao').max_length
        self.assertEquals(max_length,200)
