from django import forms
from .models import Membro


class MembroForm(forms.ModelForm):
    
    class Meta:
        model = Membro
        fields = '__all__'
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'laboratorio': forms.Select(attrs={'class': 'form-control'}),
            'membro_perfil': forms.Select(attrs={'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(MembroForm, self).__init__(*args, **kwargs)
        self.fields['laboratorio'].empty_label = "Selecione"
        self.fields['membro_perfil'].empty_label = "Selecione"