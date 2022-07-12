from django import forms
from .models import Horario



class TimeInput(forms.TimeInput):
     input_type = 'time'

class HorarioForm(forms.ModelForm):

    class Meta:
        model = Horario
        fields = '__all__'
        widgets = {

            "horario_entrada": TimeInput(attrs={'class': 'form-control'}),
            "horario_saida": TimeInput(attrs={'class': 'form-control'}),
            'turno': forms.Select(attrs={'class': 'form-control'}),
            'dia_semana': forms.Select(attrs={'class': 'form-control'}),
            'membro': forms.Select(attrs={'class': 'form-control'}),
        }

        
    def __init__(self, *args, **kwargs):
            super(HorarioForm, self).__init__(*args, **kwargs)
            self.fields['membro'].empty_label = "Selecione"
            self.fields['turno'].empty_label = "Selecione"
            