from django.forms import ModelForm
from projetos_app.models import Projeto

class ProjectForm(ModelForm):
    class Meta:
        model=Projeto
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição',
            'coordenador_projeto ': 'Coordenador',
            'participantes': 'Participantes',
            'laboratorio_projeto': 'Laboratório'
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['coordenador_projeto'].empty_label = "Selecione"
        self.fields['participantes'].empty_label = "Selecione"
        self.fields['laboratorio_projeto'].empty_label = "Selecione"