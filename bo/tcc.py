from tcc_app.models import Tcc

def get_tcc():
    return Tcc.objects.all()