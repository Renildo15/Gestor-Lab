from django.db import models
from membros_app.models import Membro


# Create your models here.
class Horario(models.Model):
    horario_entrada = models.TimeField(null=True, blank=True)
    horario_saida = models.TimeField(null=True, blank=True)
    os_choices = (
        ('Matutino', 'Matutino'),
        ('Vespertino', 'Vespertino'),
        ('Noturno', 'Noturno')
    )

    turno = models.CharField(max_length=50, choices=os_choices,null=True, blank=True)
    dia_semana = models.DateField("Purchase Date(dd/mm/2022)",null=True, blank=True)
    membro = models.ForeignKey(Membro, on_delete=models.SET_NULL, related_name='membrohorario', null=True, blank=True)

    def __str__(self):
        return self.titulo
