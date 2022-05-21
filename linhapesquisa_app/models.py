from django.db import models

# Create your models here.
class LinhaPesquisa(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.CharField(max_length=200)
    area = models.CharField(max_length=60)
    cnpq = models.CharField(max_length=60)
    
    def __str__(self):
        return self.nome
