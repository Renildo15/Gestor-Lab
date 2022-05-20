from datetime import datetime
from django.db import models
from django.forms import CharField


class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    coordenador = models.CharField(max_length=50)
    participantes = models.CharField(max_length=150)

    def __str__(self):
        return self.titulo