from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Personaliza a classe User padrão do Django 
class Usuario(AbstractUser):
	name = models.CharField(max_length=255)

# Cria um modelo para as transferencias
class Transferencia(models.Model):
	valor = models.FloatField()
	destino = models.CharField(max_length=255)
	data = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.destino
