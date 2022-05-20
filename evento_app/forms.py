from django.forms import ModelForm
from .models import Evento

class EventForm(ModelForm):
    class Meta:

        model = Evento
        fields = '__all__'
        labels = {
                'titulo': 'Nome',
                'descricao': 'E-Mail',
                'area': 'Telefone',
                'laboratorio': 'Laboratório',
                'site': 'Perfil'
        }

        def __init__(self, *args, **kwargs):
            super(EventForm, self).__init__(*args, **kwargs)
            self.fields['laboratorio'].empty_label = "Selecione"

