from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Unidade(models.Model):
    nome = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome
class DataSolicitacao(models.Model):
    data = models.DateField()

    def __str__(self):
        return self.data.strftime("%d/%m/%Y")

class Local(models.Model):   #locins
    local = models.CharField(max_length=70, verbose_name= "Local")

    def __str__(self):
        return self.local

class Comentario(models.Model):
    ocorrencia = models.ForeignKey('Ocorrencia', on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField('Texto')
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comentarios", verbose_name="Plantonista")
    def __str__(self):
        return f"Comentário de {self.autor} em {self.data_criacao.strftime('%d/%m/%Y %H:%M')}"


class Plantao(models.Model):
    class TurnoPlantao(models.TextChoices):
        DIURNO = 'DIURNO', 'Diurno'
        NOTURNO = 'NOTURNO', 'Noturno'
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    inicio = models.DateTimeField(default=timezone.now)
    turno = models.CharField(max_length=10, choices=TurnoPlantao.choices)

    class Meta:
        verbose_name_plural = 'Plantões'
        verbose_name = 'Plantão'

    def __str__(self):
        return f'{self.usuario.username} - {self.inicio.strftime('%d/%m/%Y %H:%M') } - {self.turno}'

class Ocorrencia(models.Model):
    class StatusOcorrencia(models.TextChoices):
        EM_ABERTO = 'EM_ABERTO', 'Em Aberto'
        CONCLUIDA = 'CONCLUIDA', 'Concluida'    
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name="ocorrencia")
    local = models.ForeignKey(Local, on_delete= models.CASCADE, null=True, blank=True, related_name="ocorrencia")
    titulo = models.CharField(max_length=30, verbose_name= "Título")
    data_solicitacao = models.DateTimeField(null=True, blank= True, verbose_name= 'Data da Solicitação')
    descricao = models.TextField('Descrição',blank=True, null=True)
    criticidade = models.CharField(
        max_length=20,
        choices=[('NORMAL', 'Normal'), ('URGENTE', 'Urgente'), ('EMERGENCIAL', 'Emergencial')],
        verbose_name= "Criticidade",
        default="NORMAL"
    )
    status = models.CharField(
        'Status',
        max_length=10,
        choices=StatusOcorrencia.choices,
        default=StatusOcorrencia.EM_ABERTO,
    )
    
    @property
    def em_aberto(self):
        return self.status == self.StatusOcorrencia.EM_ABERTO
    
    @property
    def concluida(self):
        return self.status == self.StatusOcorrencia.CONCLUIDA


    