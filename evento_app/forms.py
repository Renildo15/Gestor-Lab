from django.forms import ModelForm
from django import forms
from .models import Evento

class DateInput(forms.DateInput):
     input_type = 'date'

class EventForm(ModelForm):
    class Meta:

        model = Evento
        fields = '__all__'
        widgets = {
                'titulo': forms.TextInput(attrs={'class': 'form-control'}),
                'descricao': forms.Textarea(attrs={'class': 'form-control'}),
                'area': forms.TextInput(attrs={'class': 'form-control'}),
                'laboratorio': forms.Select(attrs={'class': 'form-control'}),
                'site': forms.URLInput(attrs={'class': 'form-control'}),
                'data_sbm': DateInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['laboratorio'].empty_label = "Selecione"

