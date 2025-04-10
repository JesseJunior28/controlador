from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    matricula = models.CharField(max_length=20, unique=True)
    cargo = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True)
    is_plantonista = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_full_name()} ({self.matricula})"
