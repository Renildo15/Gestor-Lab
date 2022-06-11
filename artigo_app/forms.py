from django.forms import ModelForm
from .models import Artigo

class ArtForm(ModelForm):
    class Meta:
        model = Artigo
        fields = '__all__'
        labels = {
                'titulo': 'Título',
                'autores': 'Autores',
                'local_publi': 'Local Da Publicação',
                'descricao': 'Descrição',
                'laboratorio_art': 'Laboratório'
        }

    def __init__(self, *args, **kwargs):
        super(ArtForm, self).__init__(*args, **kwargs)
        self.fields['autores'].empty_label = "Selecione"
        self.fields['laboratorio_art'].empty_label = "Selecione"