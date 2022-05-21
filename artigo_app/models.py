from django.db import models

class Artigo(models.Model):
    titulo = models.CharField(max_length=50)
    autores = models.CharField(max_length=50)
    local_Publi = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)
    
 
    def __str__(self):
        return self.titulo