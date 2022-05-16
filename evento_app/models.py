from datetime import datetime
from django.db import models
from django.forms import CharField



class Evento(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    area = models.CharField(max_length=50)
    site = models.CharField(max_length=150)
    data_sbm = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return self.titulo

