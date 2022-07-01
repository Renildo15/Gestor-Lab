from horario_app.models import Horario

def get_horario():
    return Horario.objects.all()