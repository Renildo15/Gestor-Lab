from django import forms
from .models import Horario



class TimeInput(forms.TimeInput):
     input_type = 'time'

class HorarioForm(forms.ModelForm):

    class Meta:
        model = Horario
        fields = '__all__'
        labels = {
            'horario_entrada': 'Hora Entrada',
            'horario_saida': 'Hora Saída',
            'turno': 'Turno',
            'dia_semana': 'Dia',
            'membro': 'Membro',
        }

        widgets = {

            "horario_entrada": TimeInput(),
            "horario_saida": TimeInput(),
        }

        
    def __init__(self, *args, **kwargs):
            super(HorarioForm, self).__init__(*args, **kwargs)
            self.fields['membro'].empty_label = "Selecione"
            