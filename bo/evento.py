from evento_app.models import Evento

def get_evento():
    return Evento.objects.all()