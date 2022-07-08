from django.db import models



class Estagio(models.Model):
    estagiario = models.CharField(max_length=30)
    orientador = models.CharField(max_length=30)
    supervisor = models.CharField(max_length=30)
    atividade = models.CharField(max_length=200)
    laboratorio = models.ForeignKey(to='laboratorio_app.Lab', on_delete=models.CASCADE,null=True, blank=True)
 
    def __str__(self):
        return self.estagiario
