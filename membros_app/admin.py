from django.contrib import admin
from .models import Membro, Perfil
from laboratorio_app.models import Lab
from evento_app.models import Evento

# Register your models here.

admin.site.register(Membro)
admin.site.register(Perfil)
admin.site.register(Lab)
admin.site.register(Evento)
