from django.db import models

# Create your models here.
class Produto(models.Model):
    imagem = models.ImageField(upload_to='imagens/', null=True, blank=True)
    img = models.ImageField(upload_to='produtos_imagens/')

    def __str__(self):
        return self.nome


