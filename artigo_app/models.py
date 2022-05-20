from django.db import models
from laboratorio_app.models import Lab
from membros_app.models import Membro

class Artigo(models.Model):
    titulo = models.CharField(max_length=50)
    autores = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name='autores')
    local_Publi = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)
    laboratorio_art = models.ForeignKey(Lab, on_delete=models.CASCADE, related_name='laboratorio_art')
    
 
    def __str__(self):
        return self.titulo