from django.db import models
from membros_app.models import Membro
from laboratorio_app.models import Lab


class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    coordenador_projeto = models.ForeignKey(Membro, on_delete=models.SET_NULL, related_name='coordenador_projeto', null=True, blank=True)
    participantes = models.ForeignKey(Membro, on_delete=models.SET_NULL, related_name='participantes', null=True, blank=True)
    laboratorio_projeto = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name='laboratorio_projeto', null=True, blank=True)

    def __str__(self):
        return self.titulo