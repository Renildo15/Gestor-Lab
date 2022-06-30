from django.test import TestCase
from membros_app.models import Membro, Perfil

class MembroTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Membro.objects.create(nome='Breno',
                              email='breno123@hotmail.com',
                              telefone= '84996565241')
    
    # Testes no campo "nome"
    
    def testNameLabeling(self):
        membro = Membro.objects.get(id=1)
        field_label = membro._meta.get_field('nome').verbose_name
        self.assertEquals(field_label, 'nome')
        
    def testNameLength(self):
        membro = Membro.objects.get(id=1)
        max_length = membro._meta.get_field('nome').max_length
        self.assertEquals(max_length, 60)
        
    # Testes no campo "email"
    
    def testEmailLabeling(self):
        membro = Membro.objects.get(id=1)
        field_label = membro._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')
        
    def testEmailLength(self):
        membro = Membro.objects.get(id=1)
        max_length = membro._meta.get_field('email').max_length
        self.assertEquals(max_length, 30)
    
    # Testes no campo "telefone"
    
    def testPhoneLabeling(self):
        membro = Membro.objects.get(id=1)
        field_label = membro._meta.get_field('telefone').verbose_name
        self.assertEquals(field_label, 'telefone')
        
    def testPhoneLength(self):
        membro = Membro.objects.get(id=1)
        max_length = membro._meta.get_field('telefone').max_length
        self.assertEquals(max_length, 20)
        
class PerfilTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Perfil.objects.create(titulo = 'Docente')
    
    #Teste no campo "titulo"
    
    def testTituloLabeling(self):
        perfil = Perfil.objects.get(id=1)
        field_label = perfil._meta.get_field('titulo').verbose_name
        self.assertEquals(field_label, 'titulo')
        
    def testTitleLength(self):
        perfil = Perfil.objects.get(id=1)
        max_length = perfil._meta.get_field('titulo').max_length
        self.assertEquals(max_length, 50)
