from django import forms
from .models import Tcc
class DateInput(forms.DateInput):
     input_type = 'date'
class TccForm(forms.ModelForm):

    class Meta:
        model = Tcc
        fields = '__all__'
        labels = {
            'titulo': 'Titulo',
            'autores': 'Autores',
            'orientadores': 'Orientadores',
            'descricao': 'Descricao',
        }
        widgets = {

            "dtpublicacao":   DateInput(),
        }
        
    def __init__(self, *args, **kwargs):
            super(TccForm, self).__init__(*args, **kwargs)
            self.fields['autores'].empty_label = "Selecione"
            self.fields['orientadores'].empty_label = "Selecione"
