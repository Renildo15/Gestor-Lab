from django import forms
from .models import Lab

class LabForm(forms.ModelForm):

    class Meta:
        model = Lab
        fields = '__all__'
        labels = {
            'descricao': 'Descricao',
            'nome': 'Nome',
            'coordenador': 'Coordenador',
            'vice_coordenador': 'Vice Coordenador',
        }
        
    def __init__(self, *args, **kwargs):
        super(LabForm, self).__init__(*args, **kwargs)
        self.fields['coordenador'].required = False
        self.fields['vice_coordenador'].required = False
        self.fields['coordenador'].empty_label = "Selecione"
        self.fields['vice_coordenador'].empty_label = "Selecione"
        