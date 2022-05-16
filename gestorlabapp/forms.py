from dataclasses import fields
from django.forms import ModelForm
from gestorlabapp.models import Lab

class LabForm(ModelForm):
    class Meta:
        model=Lab
        fields = ['descricao','nome','coordenador','vice_coordenador']

