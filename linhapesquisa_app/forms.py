from django import forms
from .models import LinhaPesquisa


class LinhaForm(forms.ModelForm):
    
    class Meta:
        model = LinhaPesquisa
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'areaCNPQ': forms.TextInput(attrs={'class': 'form-control'}),
            'subAreaCNPQ': forms.TextInput(attrs={'class': 'form-control'}),
            'laboratorio_pesq': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(LinhaForm, self).__init__(*args, **kwargs)
        self.fields['laboratorio_pesq'].empty_label = "Selecione"
        
    