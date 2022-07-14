from django.forms import ModelForm
from .models import Artigo
from django import forms

class ArtForm(ModelForm):
    class Meta:
        model = Artigo
        fields = '__all__'
        widgets = {
                'titulo': forms.TextInput(attrs={'class': 'form-control'}),
                'autores': forms.Select(attrs={'class': 'form-control'}),
                'local_Publi': forms.URLInput(attrs={'class': 'form-control'}),
                'descricao': forms.Textarea(attrs={'class': 'form-control'}),
                'laboratorio_art': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ArtForm, self).__init__(*args, **kwargs)
        self.fields['autores'].empty_label = "Selecione"
        self.fields['laboratorio_art'].empty_label = "Selecione"