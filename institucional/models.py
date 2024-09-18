from django.db import models

# Create your models here.

class RedesSociais(models.Model):
    nome = models.CharField(max_length=200)
    link = models.CharField(max_length=2000)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome}"