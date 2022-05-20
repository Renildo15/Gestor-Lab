from dataclasses import fields
from tkinter import E
from django.forms import ModelForm
from projetos_app.models import Projeto

class ProjectForm(ModelForm):
    class Meta:
        model=Projeto
        fields = ['nome','descricao','coordenador','participantes']