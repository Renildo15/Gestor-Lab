from django.db import models
from membros_app.models import Membro
from linhapesquisa_app.models import LinhaPesquisa


# Create your models here.
class Tcc(models.Model):
    titulo = models.CharField(max_length=50)
    autores = models.ForeignKey(Membro, on_delete=models.SET_NULL, related_name='autorestcc', null=True, blank=True)
    orientadores = models.ForeignKey(Membro, on_delete=models.SET_NULL, related_name='orientadorestcc', null=True, blank=True)
    dtpublicacao = models.DateField()
    instituicao = models.CharField(max_length=50)
    descricao = models.TextField()
    pesquisa = models.ForeignKey(LinhaPesquisa, on_delete=models.SET_NULL, related_name='pesquisa', null=True, blank=True)
    def __str__(self):
        return self.titulo


