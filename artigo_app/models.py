from django.db import models
from laboratorio_app.models import Lab
from usuarios_app.models import Discente

class Artigo(models.Model):
    titulo = models.CharField(max_length=50)
    autores = models.ForeignKey(Discente, on_delete=models.CASCADE, related_name='autores')
    local_Publi = models.URLField(max_length=200)
    descricao = models.TextField()
    laboratorio_art = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name='laboratorio_art')
    
 
    def __str__(self):
        return self.titulo