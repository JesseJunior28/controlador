from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError



class Unidade(models.Model):
    nome = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome

class Planta(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Ativo(models.Model):
    codigo = models.CharField(max_length=50)

    def __str__(self):
        return self.codigo


class LocalExterno(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(
        "Localização",
        max_length=200,
        blank=True,
        help_text="Localização do local"
    )
    endereco = models.CharField(
        "Endereço",
        max_length=300,
        blank=True,
        help_text="Endereço completo"
    )

    def __str__(self):
        return self.nome


class LocalInterno(models.Model):
    planta = models.ForeignKey(
        Planta,
        on_delete=models.PROTECT,
        related_name="locais_internos"
    )
    ativo = models.ForeignKey(
        Ativo,
        on_delete=models.PROTECT,
        related_name="locais_internos"
    )

    class Meta:
        verbose_name = "Local Interno"
        verbose_name_plural = "Locais Internos"
        
    def __str__(self):
        return f'{self.planta} - {self.ativo}'

class Comentario(models.Model):
    ocorrencia = models.ForeignKey(
        'Ocorrencia',
        on_delete=models.CASCADE,
        related_name='comentarios'
    )
    texto = models.TextField('Texto')
    data_criacao = models.DateTimeField('Criado em', auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="comentarios",
        verbose_name="Plantonista"
    )

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        ordering = ('-data_criacao',)
        get_latest_by = 'data_criacao'

    @property
    def autor(self):
        # Esse alias permite usar comentario.autor no template
        return self.user.username if self.user else "Anônimo"

    def __str__(self):
        # Use self.autor aqui
        return f"Comentário de {self.autor} em {self.data_criacao:%d/%m/%Y %H:%M}"



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
        return f"{self.usuario.username} - {self.inicio.strftime('%d/%m/%Y %H:%M') } - {self.turno}"

class Ocorrencia(models.Model):
    
    EM_ABERTO = 'EM_ABERTO'
    CONCLUIDA = 'CONCLUIDA'
    CANCELADA = 'CANCELADA'

    STATUS_CHOICES = (
        (EM_ABERTO, 'Em Aberto'),
        (CONCLUIDA, 'Concluida'),
        (CANCELADA, 'Cancelada')
    )


    unidade = models.ForeignKey(
        Unidade,
        on_delete=models.CASCADE,
        related_name="ocorrencias"
    )

    local_interno = models.ForeignKey(
        'LocalInterno',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="ocorrencias_internas",
        verbose_name="Local Interno"
    )

    local_externo = models.ForeignKey(
        'LocalExterno',
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name="ocorrencias_externas",
        verbose_name="Local Externo"
    )
    ordem_de_servico = models.CharField('OS', max_length=13)

    titulo = models.CharField(max_length=30, verbose_name="Título")

    data_solicitacao = models.DateTimeField(
        null=False, blank=False, verbose_name='Data da Solicitação'
    )

    descricao = models.TextField('Descrição', blank=False, null=False)

    criticidade = models.CharField(
        max_length=20,
        blank=False,
        choices=[
            ('NORMAL', 'Normal'),
            ('URGENTE', 'Urgente'),
            ('EMERGENCIAL', 'Emergencial')
        ],
        verbose_name="Criticidade",
        default="NORMAL"

    )

    status = models.CharField(
        'Status',
        max_length=10,
        choices=STATUS_CHOICES,
        default=EM_ABERTO,
    )



    @property
    def em_aberto(self):
        return self.status == self.EM_ABERTO
    
    @property
    def ta_conluida(self):
        print(self.id, self.status == self.CONCLUIDA)
        return self.status == self.CONCLUIDA


    def __str__(self):
        local = self.local_interno or self.local_externo or "Sem local"
        return f"{self.get_status_display()} em {local}: {self.titulo}"


