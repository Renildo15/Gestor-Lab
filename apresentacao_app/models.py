from mailbox import FormatError
from tkinter import CASCADE
from django.db import models
from membros_app.models import Membro

# Create your models here.

class Apresentacao(models.Model):
    titulo = models.CharField(max_length=50)
    autores = models.ForeignKey(Membro, on_delete=models.SET_NULL, related_name='autoresApresentacao', null=True, blank=True)
    dataApresentacao = models.DateField()
    descricao = models.CharField(max_length=150)
    def __str__(self):
        return self.titulo
