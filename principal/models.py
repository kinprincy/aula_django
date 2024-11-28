from django.db import models

# Create your models here.
class Produto(models.Model):
    imagem = models.ImageField(upload_to='imagens/', null=True, blank=True)

