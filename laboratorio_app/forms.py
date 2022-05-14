from django import forms
from .models import Lab

class LabForm(forms.ModelForm):
    class Meta:
        model=Lab
        fields = ['descricao','nome','coordenador','vice_coordenador']