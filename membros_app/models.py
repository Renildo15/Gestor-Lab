from django.db import models
from laboratorio_app.models import Lab

# Create your models here.

class Perfil(models.Model):
    titulo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.titulo



class Membro(models.Model):
    nome = models.CharField(max_length=60)
    email = models.CharField(max_length=30)
    telefone = models.CharField(max_length=20)
    laboratorio = models.ForeignKey(Lab, on_delete=models.CASCADE)
    membro_perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome