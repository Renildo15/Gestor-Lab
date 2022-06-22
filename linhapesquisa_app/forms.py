from django import forms
from .models import LinhaPesquisa


class LinhaForm(forms.ModelForm):
    
    class Meta:
        model = LinhaPesquisa
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição',
            'area': 'Área',
            'cnpq': 'CNPQ',
            'laboratório': 'Laboratório'
        }

    def __init__(self, *args, **kwargs):
        super(LinhaForm, self).__init__(*args, **kwargs)
        self.fields['laboratorio_pesq'].empty_label = "Selecione"
        
    