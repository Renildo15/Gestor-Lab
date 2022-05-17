from django.contrib import admin
from .models import Membro, Perfil
from laboratorio_app.models import Lab

# Register your models here.

admin.site.register(Membro)
admin.site.register(Perfil)
admin.site.register(Lab)
