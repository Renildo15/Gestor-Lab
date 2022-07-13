from django import forms
from .models import Apresentacao

class DateInput(forms.DateInput):
     input_type = 'date'

class ApresentacaoForm(forms.ModelForm):

    class Meta:
        model = Apresentacao
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            "dataApresentacao": DateInput(attrs={'class': 'form-control'}),
            'autores': forms.Select(attrs={'class': 'form-control'}),
            'projeto': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'})
        }


    def __init__(self, *args, **kwargs):
            super(ApresentacaoForm, self).__init__(*args, **kwargs)
            self.fields['autores'].empty_label = "Selecione"
            self.fields['projeto'].empty_label = "Selecione"