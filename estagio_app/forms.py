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
        }

    def __init__(self, *args, **kwargs):
        super(estForm, self).__init__(*args, **kwargs)
