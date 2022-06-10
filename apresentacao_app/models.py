from django.db import models
from membros_app.models import Membro
from linhapesquisa_app.models import LinhaPesquisa

# Create your models here.

class Apresentacao(models.Model):
    titulo = models.CharField(max_length=50)
    autores = models.ForeignKey(Membro, on_delete=models.SET_NULL, related_name='autoresApresentacao', null=True, blank=True)
    dataApresentacao = models.DateField()
    descricao = models.TextField()
    pesquisa = models.ForeignKey(LinhaPesquisa, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.titulo
