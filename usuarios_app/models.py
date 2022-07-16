from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Docente(models.Model):
    siape = models.IntegerField(unique=True)
    nome = models.CharField(max_length=200)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    formacao = models.CharField(max_length=300)
    tipo_jornada_trabalho = models.CharField(max_length=50)
    vinculo = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    classe_funcional = models.CharField(max_length=50)
    id_unidade_lotacao = models.IntegerField()
    lotacao = models.CharField(max_length=150)
    admissao = models.DateField(blank=True, null=True)
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    def primeiro_nome(self):
        split_nome = self.nome.split(' ')
        return split_nome[0]
        
    def __str__(self):
        return self.nome + ' (' + str(self.siape) + ')'
class Discente(models.Model):
    """
    Modelo para os dados dos Discentes.
    """
    matricula = models.CharField(max_length=15, unique=True)
    nome_discente = models.CharField(max_length=200, null=False)
    sexo = models.CharField(max_length=1, blank=True)
    ano_ingresso = models.IntegerField()
    periodo_ingresso = models.IntegerField()
    forma_ingresso = models.CharField(max_length=100)
    tipo_discente = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    sigla_nivel_ensino = models.CharField(max_length=5)
    nivel_ensino = models.CharField(max_length=50)
    id_curso = models.CharField(max_length=100)
    nome_curso = models.CharField(max_length=200, null=False)
    modalidade_educacao = models.CharField(max_length=50)
    id_unidade = models.IntegerField()
    nome_unidade = models.CharField(max_length=200)
    id_unidade_gestora = models.IntegerField()
    nome_unidade_gestora = models.CharField(max_length=200)
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    def __str__(self):
        return self.nome_discente + ' (' + self.matricula.__str__() + ') - ' \
               + self.nome_curso + ' (' + self.nome_unidade + ')'


class FuncaoGratificada(models.Model):
    siape = models.IntegerField()
    nome = models.CharField(max_length=200)
    situacao_servidor = models.CharField(max_length=25)
    id_unidade = models.IntegerField()
    lotacao = models.CharField(max_length=200)
    sigla = models.CharField(max_length=15)
    inicio = models.DateField()
    fim = models.DateField(null=True)
    id_unidade_designacao = models.IntegerField()
    unidade_designacao = models.CharField(max_length=200)
    atividade = models.CharField(max_length=100)
    observacoes = models.CharField(max_length=500, null=True)
    class Meta:
        unique_together = ('siape', 'id_unidade', 'inicio', 'atividade')
    def __str__(self):
        return self.nome + ' (' + self.siape.__str__() + ') - ' \
               + self.atividade + ' (' + self.unidade_designacao + ')'