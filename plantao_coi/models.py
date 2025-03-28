from django.db import models

# Create your models here.

class Unidade(models.Model):
    nome = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome

class Local(models.Model):   #locins
    local = models.CharField(max_length=70, verbose_name= "Local")

    def __str__(self):
        return self.local

class Comentario(models.Model):
    ocorrencia = models.ForeignKey('Ocorrencia', on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor} em {self.data_criacao.strftime('%d/%m/%Y %H:%M')}"

class Ocorrencia(models.Model):
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name="ocorrencia")
    local = models.ForeignKey(Local, on_delete= models.CASCADE, related_name="ocorrencia")
    criticidade = models.CharField(
    max_length=20,
    choices=[('NORMAL', 'Normal'), ('URGENTE', 'Urgente'), ('EMERGENCIAL', 'Emergencial')],
    verbose_name= "Criticidade",
    default="NORMAL"
)
    titulo = models.CharField(max_length=30, verbose_name= "Título")
    descricao = models.TextField(verbose_name="Descrição da Ocorrência")
    status = models.CharField(max_length=20, choices=[('PENDENTE', 'Pendente'), ('EM ANDAMENTO', 'Em Andamento'), ('ENCERRADA', 'Encerrada')])
    data_abertura = models.DateTimeField(auto_now_add=True, verbose_name="Data de abertura")  
    data_encerramento = models.DateTimeField(null=True, blank=True, verbose_name="Data de Encerramento")

    def __str__(self):
        return f"Ocorrencia{self.id} - {self.titulo}"
    
    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"
        
