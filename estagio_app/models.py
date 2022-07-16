from django.db import models
from laboratorio_app.models import Lab
from usuarios_app.models import Discente, Docente



class Estagio(models.Model):
    estagiario = models.ForeignKey(Discente, on_delete=models.CASCADE, related_name="membro_estagiario")
    orientador = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name="membro_orientador")
    supervisor = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name="membro_supervisor")
    atividade = models.CharField(max_length=200)
    laboratorio = models.ForeignKey(to='laboratorio_app.Lab', on_delete=models.CASCADE)
 
    def __str__(self):
        return self.estagiario
