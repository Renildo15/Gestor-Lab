from django.forms import ModelForm
from projetos_app.models import Projeto
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model=Projeto
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'coordenador_projeto': forms.Select(attrs={'class': 'form-control'}),
            'participantes': forms.Select(attrs={'class': 'form-control'}),
            'laboratorio_projeto': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['coordenador_projeto'].empty_label = "Selecione"
        self.fields['participantes'].empty_label = "Selecione"
        self.fields['laboratorio_projeto'].empty_label = "Selecione"