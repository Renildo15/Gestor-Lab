from artigo_app.models import Artigo

def get_artigo():
    return Artigo.objects.all()