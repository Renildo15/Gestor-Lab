from membros_app.models import Membro

def get_membro():
    return Membro.objects.all()