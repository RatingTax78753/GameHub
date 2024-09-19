from django.db import models
from django.contrib.auth.models import User
import os
import django

# Create your models here.
CLASSIFICACOES = (
    ("Livre", "Livre"),
    ("10 Anos", "10 Anos"),
    ("12 Anos", "12 Anos"),
    ("14 Anos", "14 Anos"),
    ("16 Anos", "16 Anos"),
    ("18 Anos", "18 Anos"),
)

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=200, null=True, blank=True, unique=True)
    foto_perfil = models.ImageField(upload_to="Loja/Cliente/FotoPerfil", null=True, blank=True)
    lista_desejos = models.ManyToManyField("Produto", blank=True)

    def __str__(self):
        return f"{self.usuario} | Telefone: {self.telefone}"
    

class TipoProduto(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    codigo_cor = models.CharField(max_length=50)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f"{self.nome}"
    

class Franquia(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return f"{self.nome}"
    

class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return f"{self.nome}"
    
    
class Distribuidora(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return f"{self.nome}"


class Plataforma(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    codigo_cor = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="Loja/Plataformas/")

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return f"{self.nome}"
    

class Sistema(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    plataforma = models.ForeignKey(Plataforma, null=True, on_delete=models.SET_NULL, related_name="plataforma")

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return f"{self.nome}"


class Ativacao(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=200)

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return f"{self.nome}"


class Categoria(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    codigo_cor = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to="Loja/Categorias/")

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return f"{self.nome}"
    

class Gameplay(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['slug']

    def __str__(self):
        return f"{self.nome}"
    

class Produto(models.Model):
    ativo = models.BooleanField(default=True)
    tipo = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)
    franquia = models.ForeignKey(Franquia, null=True, blank=True, on_delete=models.CASCADE)
    capa = models.ImageField(upload_to="Loja/Produtos")
    trailer = models.CharField(max_length=500)
    nome = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    descricao = models.TextField(default="")
    lancamento = models.DateField(default=django.utils.timezone.now)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    desenvolvedora = models.ForeignKey(Desenvolvedora, on_delete=models.CASCADE)
    distribuidora = models.ForeignKey(Distribuidora, on_delete=models.CASCADE)
    categorias = models.ManyToManyField("Categoria")
    gameplay = models.ManyToManyField("Gameplay")
    sistemas = models.ManyToManyField("Sistema")
    ativacao = models.ForeignKey(Ativacao, null=True, on_delete=models.SET_NULL)
    classificacao = models.CharField(max_length=100, choices=CLASSIFICACOES)
    quantidade_vendida = models.IntegerField(default=0)

    class Meta:
        ordering = ['-tipo', 'nome']

    def __str__(self):
        return f"{self.nome} | {self.tipo}"


class EstoqueProduto(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, related_name="estoque_produto")
    quantidade = models.IntegerField(default=0)

    class Meta:
        ordering = ['produto']

    def __str__(self):
        return f"{self.produto.tipo} | Produto: {self.produto.nome} | Quantidade: {self.quantidade}"


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.SET_NULL)
    finalizado = models.BooleanField(default=False)
    codigo_transacao = models.CharField(max_length=200, null=True, blank=True)
    data_finalizacao = models.DateTimeField(null=True, blank=True)
    preco_final = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    @property
    def preco_total(self):
        itens_pedido = ItensPedido.objects.filter(pedido__id=self.id)
        preco = sum([item.preco_total for item in itens_pedido])
        return preco
            
    def save(self, *args, **kwargs):
        if self.finalizado:
            self.data_finalizacao = django.utils.timezone.now()
            super().save(*args, **kwargs)
            for item in ItensPedido.objects.filter(pedido=self):
                produto = item.estoque_produto.produto
                estoque = item.estoque_produto

                produto.quantidade_vendida += 1
                estoque.quantidade -= 1

                produto.save()
                estoque.save()
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return f"Cliente: {self.cliente} |Código Transação: {self.codigo_transacao} | Finalizado: {self.finalizado}"

class Chave(models.Model):
    chave = models.CharField(max_length=100)
    produto = models.ForeignKey(Produto, null=True, blank=True, on_delete=models.SET_NULL, related_name="chave")
    ativacao = models.ForeignKey(Ativacao, null=True, on_delete=models.SET_NULL, related_name="chave")

    def __str__(self):
        return f'Chave para o produto {self.produto.nome}'

class ItensPedido(models.Model):
    estoque_produto = models.ForeignKey(EstoqueProduto, null=True, blank=True, on_delete=models.SET_NULL, related_name="itens_pedido")
    no_carrinho = models.BooleanField(default=False)
    chave_liberada = models.BooleanField(default=False)
    pedido = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.SET_NULL, related_name="itens_pedido")
    chave = models.OneToOneField(Chave, null=True, blank=True, on_delete=models.SET_NULL, related_name="itens_pedido")

    def __str__(self):
        return f'ID pedido: {self.pedido.id} | Produto: {self.estoque_produto.produto.nome}'

    @property
    def preco_total(self):
        return self.estoque_produto.produto.preco
    
class Pagamento(models.Model):
    id_pagamento = models.CharField(max_length=400)
    pedido = models.ForeignKey(Pedido, null=True, blank=True, on_delete=models.SET_NULL, related_name="pagamento_pedido")
    link_pagamento = models.URLField(max_length=1000, default="")
    aprovado = models.BooleanField(default=False)
    metodo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.pedido} | ID: {self.id_pagamento}"