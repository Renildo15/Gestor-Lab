from django import forms
from .models import LinhaPesquisa


class linhaForm(forms.ModelForm):
    
    class Meta:
        model = LinhaPesquisa
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição',
            'area': 'Área',
            'cnpq': 'CNPQ',
        }
        
    