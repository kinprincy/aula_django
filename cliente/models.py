from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=60)
    def __str__(self):
        return self.nome

    telefone = models.CharField(max_length=15)
    def __str__(self):
        return self.telefone

    email = models.CharField(max_length=60)
    def __str__(self):
        return self.email