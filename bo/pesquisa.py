from linhapesquisa_app.models import LinhaPesquisa

def get_pesquisa():
    return LinhaPesquisa.objects.all()