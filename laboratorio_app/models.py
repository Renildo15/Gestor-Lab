from django.db import models

class Lab(models.Model):
    descricao = models.CharField(max_length=60)
    nome = models.CharField(max_length=60)
    ##Aqui deve ser uma chave estrangeira, com o id do membro que coordenador e vice-coordenador. Como ainda não foi cria a classe membros, coloquei
    ##como 'IntegerField()' para que o sistema funcionasse. Deve ser corrigido assim que a classe for criada.
    coordenador = models.CharField(max_length=60)
    vice_coordenador = models.CharField(max_length=60)
    
    def __str__(self):
        return self.nome



