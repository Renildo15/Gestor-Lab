from django.db.models import Q
from laboratorio_app.models import Lab

def get_laboratorio():
    return Lab.objects.all()