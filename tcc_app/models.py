from mailbox import FormatError
from tkinter import CASCADE
from django.db import models
from membros_app.models import Membro


# Create your models here.
class Tcc(models.Model):
    titulo = models.CharField(max_length=50)
    autores = models.ForeignKey(Membro, on_delete=models.SET_NULL, related_name='autorestcc', null=True, blank=True)
    orientadores = models.ForeignKey(Membro, on_delete=models.SET_NULL, related_name='orientadorestcc', null=True, blank=True)
    dtpublicacao = models.DateField()
    descricao = models.CharField(max_length=150)
    def __str__(self):
        return self.titulo


