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
                'descricao': 'Descrição'
        }