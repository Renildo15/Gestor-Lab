from django.forms import ModelForm
from .models import Estagio
from django import forms

class EstForm(ModelForm):
    class Meta:

        model = Estagio
        fields = '__all__'
        widgets = {
                'estagiario': forms.Select(attrs={'class': 'form-control'}),
                'orientador': forms.Select(attrs={'class': 'form-control'}),
                'supervisor': forms.Select(attrs={'class': 'form-control'}),
                'atividade': forms.TextInput(attrs={'class': 'form-control'}),
                'laboratorio': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EstForm, self).__init__(*args, **kwargs)
        self.fields['laboratorio'].empty_label = "Selecione"
        self.fields['estagiario'].empty_label = "Selecione"
        self.fields['supervisor'].empty_label = "Selecione"
        self.fields['orientador'].empty_label = "Selecione"
