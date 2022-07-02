from projetos_app.models import Projeto

def get_projeto():
    return Projeto.objects.all()