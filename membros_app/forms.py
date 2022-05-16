from django import forms
from .models import Membro


class MembroForm(forms.ModelForm):
    
    class Meta:
        model = Membro
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'email': 'E-Mail',
            'telefone': 'Telefone',
            'laboratorio': 'Laboratório',
            'membro_perfil': 'Perfil'
        }
        
    def __init__(self, *args, **kwargs):
        super(MembroForm, self).__init__(*args, **kwargs)
        self.fields['laboratorio', 'membro_perfil'].empty_label = "Selecione"