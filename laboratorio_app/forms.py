from django import forms
from .models import Lab

class LabForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = '__all__'

        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control'}),
            'sigla' : forms.TextInput(attrs={'class': 'form-control'}),
            'coordenador': forms.Select(attrs={'class': 'form-control'}),
            'vice_coordenador': forms.Select(attrs={'class': 'form-control'}),
            'descricao' : forms.Textarea(attrs={'class': 'form-control'})
        }
        
    def __init__(self, *args, **kwargs):
        super(LabForm, self).__init__(*args, **kwargs)
        self.fields['coordenador'].required = False
        self.fields['vice_coordenador'].required = False
        self.fields['coordenador'].empty_label = "Selecione"
        self.fields['vice_coordenador'].empty_label = "Selecione"
        