from django.forms import ModelForm
from .models import Estagio

class estForm(ModelForm):
    class Meta:

        model = Estagio
        fields = '__all__'
        labels = {
                'estagiario': 'Nome',
                'orientador': 'Nome',
                'supervisor': 'Nome',
                'atividade': 'Atividade',
                'laboratorio': 'Laboratorio',
        }

    def __init__(self, *args, **kwargs):
        super(estForm, self).__init__(*args, **kwargs)
        self.fields['laboratorio'].empty_label = "Selecione"
        self.fields['estagiario'].empty_label = "Selecione"
        self.fields['supervisor'].empty_label = "Selecione"
        self.fields['orientador'].empty_label = "Selecione"
