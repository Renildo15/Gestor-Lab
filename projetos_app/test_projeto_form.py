from django.test import TestCase
from projetos_app.forms import ProjectForm

class ProjetoFormTestCase(TestCase):

    def test_projeto_form_valido(self):
        form = ProjectForm(data={
            'Nome':'Projeto 01',
            'Descrição': 'teste',
            'Coordenador': 1,
            'Participantes': 1,
            'Laboratório': 1,
            
        })

        self.assertTrue(form.errors)

    def test_projeto_form_invalido(self):
        form = ProjectForm(data={})
        self.assertFalse(form.is_valid())