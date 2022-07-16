from django.db import models
from usuarios_app.models import Discente, Docente
from laboratorio_app.models import Lab


class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    coordenador_projeto = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='coordenador_projeto')
    participantes = models.ForeignKey(Discente, on_delete=models.SET_NULL, related_name='participantes', null=True, blank=True)
    laboratorio_projeto = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name='laboratorio_projeto')
    descricao = models.TextField()

    def __str__(self):
        return self.nome