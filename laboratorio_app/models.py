from django.db import models
from membros_app.models import Membro
class Lab(models.Model):
    nome = models.CharField(max_length=60)
    sigla = models.CharField(max_length=25, unique=True, null=True, blank=True)
    coordenador = models.ForeignKey(Membro,on_delete=models.SET_NULL, related_name='coordenador', null=True, blank=True)
    vice_coordenador = models.ForeignKey(Membro, on_delete=models.SET_NULL, related_name='vice_coordenador', null=True, blank=True)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome



