from django.db import models
from laboratorio_app.models import Lab

# Create your models here.
class LinhaPesquisa(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.TextField(max_length=200)
    areaCNPQ = models.CharField(max_length=150,null=True, blank=True)
    subAreaCNPQ = models.CharField(max_length=150,null=True, blank=True)
    laboratorio_pesq = models.ForeignKey(Lab,on_delete=models.CASCADE, related_name='laboratorio_pesq',null=True, blank=True)
    
    def __str__(self):
        return self.nome
