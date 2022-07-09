from django.db import models
from laboratorio_app.models import Lab
from membros_app.models import Membro



class Estagio(models.Model):
    estagiario = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name="membro_estagiario")
    orientador = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name="membro_orientador")
    supervisor = models.ForeignKey(Membro, on_delete=models.CASCADE, related_name="membro_supervisor")
    atividade = models.CharField(max_length=200)
    laboratorio = models.ForeignKey(to='laboratorio_app.Lab', on_delete=models.CASCADE)
 
    def __str__(self):
        return self.estagiario
