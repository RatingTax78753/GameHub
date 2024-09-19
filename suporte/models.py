from django.db import models
from loja.models import User
import django

# Create your models here.

NOTAS = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)

class Topico(models.Model):
    nome = models.CharField(max_length=200, default="")
    slug = models.CharField(max_length=200, default="")
    simbolo = models.ImageField(upload_to="Suporte/Topico/", null=True, blank=True)

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return f"{self.nome}"


class ConteudoTopico(models.Model):
    posicao = models.IntegerField(default=1)
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE, related_name="conteudo_topico")
    titulo = models.CharField(max_length=2000)
    conteudo = models.TextField(default="")

    class Meta:
        ordering = ['topico', 'posicao']

    def __str__(self):
        return f"{self.topico} | {self.titulo} "
    

class Pergunta(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    pergunta = models.CharField(max_length=5000)
    data = models.DateTimeField(default=django.utils.timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} | {self.autor}"


class Resposta(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, null=True, blank=True, related_name="respostas")
    resposta = models.CharField(max_length=10000)
    data = models.DateTimeField(default=django.utils.timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Resposta de {self.autor} para a pergunta: {self.pergunta.titulo}"


class Feedback(models.Model):
    nota = models.CharField(choices=NOTAS, max_length=200)
    motivo = models.CharField(max_length=5000, null=True, blank=True)
    data = models.DateField(default=django.utils.timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Nota: {self.nota} | {self.autor}"
