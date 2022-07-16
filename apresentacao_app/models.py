from django.db import models
from usuarios_app.models import Docente, Discente
from projetos_app.models import Projeto

# Create your models here.

class Apresentacao(models.Model):
    titulo = models.CharField(max_length=50)
    autores = models.ForeignKey(Discente, on_delete=models.CASCADE, related_name='autoresApresentacao')
    dataApresentacao = models.DateField()
    descricao = models.TextField()
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo
