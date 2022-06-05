from django.db import models
from membros_app.models import Membro


# Create your models here.
class Horario(models.Model):
    dia = models.IntegerField()
    turno = models.CharField(max_length=1)
    horario = models.IntegerField()
    membro = models.ForeignKey(Membro, on_delete=models.SET_NULL, related_name='membrohorario', null=True, blank=True)

    def __str__(self):
        return self.titulo
