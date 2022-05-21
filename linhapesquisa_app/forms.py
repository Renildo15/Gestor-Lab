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
            'laboratório': 'Laboratório'
        }

        def __init__(self, *args, **kwargs):
            super(linhaForm, self).__init__(*args, **kwargs)
            self.fields['laboratorio'].empty_label = "Selecione"
        
    