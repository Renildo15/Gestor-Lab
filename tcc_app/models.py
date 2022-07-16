from django.db import models
from usuarios_app.models import Discente, Docente
from linhapesquisa_app.models import LinhaPesquisa


# Create your models here.
class Tcc(models.Model):
    titulo = models.CharField(max_length=50)
    autores = models.ForeignKey(Discente, on_delete=models.CASCADE, related_name='autorestcc')
    orientadores = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='orientadorestcc')
    dtpublicacao = models.DateField()
    instituicao = models.CharField(max_length=50)
    descricao = models.TextField()
    pesquisa = models.ForeignKey(LinhaPesquisa, on_delete=models.CASCADE, related_name='pesquisa')
    def __str__(self):
        return self.titulo


