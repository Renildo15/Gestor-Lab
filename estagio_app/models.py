from django.db import models



class Estagio(models.Model):
    estagiario = models.CharField(max_length=30)
    orientador = models.CharField(max_length=30)
    supervisor = models.CharField(max_length=30)
    atividade = models.URLField(max_length=200)
 
    def __str__(self):
        return self.estagiario
