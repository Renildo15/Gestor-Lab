from dataclasses import fields
from tkinter import E
from django.forms import ModelForm
from projetos_app.models import Projeto

class ProjectForm(ModelForm):
    class Meta:
        model=Projeto
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição',
            'coordenador': 'Coordenador',
            'participantes': 'Participantes',
            'laboratorio': 'Laboratório'
        }

        def __init__(self, *args, **kwargs):
            super(ProjectForm, self).__init__(*args, **kwargs)
            self.fields['coordenador'].empty_label = "Selecione"
            self.fields['participantes'].empty_label = "Selecione"
            self.fields['laboratorio'].empty_label = "Selecione"