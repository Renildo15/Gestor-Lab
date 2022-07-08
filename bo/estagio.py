from estagio_app.models import Estagio

def get_estagio():
    return Estagio.objects.all()