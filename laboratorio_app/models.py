from django.db import models
from membros_app.models import Membro
class Lab(models.Model):
    descricao = models.CharField(max_length=60)
    nome = models.CharField(max_length=60)
    coordenador = models.ForeignKey(Membro,on_delete=models.SET_NULL, related_name='coordenador', null=True, blank=True)
    vice_coordenador = models.ForeignKey(Membro, on_delete=models.SET_NULL, related_name='vice_coordenador', null=True, blank=True)
    
    def __str__(self):
        return self.nome



