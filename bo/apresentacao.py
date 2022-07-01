from apresentacao_app.models import Apresentacao

def get_apresentacao():
    return Apresentacao.objects.all()