from django.db import models
from laboratorio_app.models import Lab



class Evento(models.Model):
    titulo = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    laboratorio = models.ForeignKey(Lab, on_delete=models.CASCADE,null=True, blank=True )
    site = models.URLField(max_length=200)
    data_sbm = models.DateField(auto_now_add=True)
    descricao = models.TextField()
 
    def __str__(self):
        return self.titulo

