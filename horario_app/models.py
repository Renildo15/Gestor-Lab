from django.db import models
from membros_app.models import Membro


# Create your models here.
class Horario(models.Model):
    horario_entrada = models.TimeField()
    horario_saida = models.TimeField()
    os_choices = (
        ('Matutino', 'Matutino'),
        ('Vespertino', 'Vespertino'),
        ('Noturno', 'Noturno')
    )
    dias_choices =(
        ('Segunda-Feira','Segunda-Feira'),
        ('Terça-Feira','Terça-Feira'),
        ('Quarta-Feira','Quarta-Feira'),
        ('Quinta-Feira','Quinta-Feira'),
        ('Sexta-Feira','Sexta-Feira'),
        ('Sabádo','Sabádo'),
        ('Domingo','Domingo'),
    )
    turno = models.CharField(max_length=50, choices=os_choices)
    dia_semana = models.CharField(max_length=50,choices=dias_choices)
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='membrohorario')

    def __str__(self):
        return self.titulo
