from django import forms
from .models import Apresentacao

class ApresentacaoForm(forms.ModelForm):

    class Meta:
        model = Apresentacao
        fields = '__all__'
        labels = {
            'titulo': 'Titulo',
            'autores': 'Autores',
            'descricao': 'Descricao',

        }
        widgets = {

            "dataApresentacao":   forms.DateInput(),
        }


    def __init__(self, *args, **kwargs):
            super(ApresentacaoForm, self).__init__(*args, **kwargs)
            self.fields['autores'].empty_label = "Selecione"