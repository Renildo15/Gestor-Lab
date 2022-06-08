from django import forms
from .models import Horario

class HorarioForm(forms.ModelForm):

    class Meta:
        model = Horario
        fields = '__all__'
        labels = {
            'dia': 'Dia',
            'turno': 'Turno',
            'horario': 'Horario',
            'membro': 'Membro',

        }

        
    def __init__(self, *args, **kwargs):
            super(HorarioForm, self).__init__(*args, **kwargs)
            self.fields['membro'].empty_label = "Selecione"
            