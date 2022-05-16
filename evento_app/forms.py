from dataclasses import fields
from tkinter import E
from django.forms import ModelForm
from evento_app.models import Evento

class EventForm(ModelForm):
    class Meta:
        model=Evento
        fields = ['titulo','descricao','area','site']

