from django.db import models

# Create your models here.

class Perfil(models.Model):
    titulo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.titulo



class Membro(models.Model):
    nome = models.CharField(max_length=60)
    email = models.CharField(max_length=30)
    telefone = models.CharField(max_length=20)
    membro_perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)