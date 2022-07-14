from django import forms
from .models import Tcc
class DateInput(forms.DateInput):
     input_type = 'date'
class TccForm(forms.ModelForm):

    class Meta:
        model = Tcc
        fields = '__all__'
        widgets = {

            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autores': forms.Select(attrs={'class': 'form-control'}),
            'orientadores': forms.Select(attrs={'class': 'form-control'}),
            'instituicao': forms.TextInput(attrs={'class': 'form-control'}),
            "dtpublicacao": DateInput(attrs={'class': 'form-control'}),
            'pesquisa': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'})
        }
        
    def __init__(self, *args, **kwargs):
            super(TccForm, self).__init__(*args, **kwargs)
            self.fields['autores'].empty_label = "Selecione"
            self.fields['orientadores'].empty_label = "Selecione"
            self.fields['pesquisa'].empty_label = "Selecione"
