from django.db.models import Max, Min
from .models import *
from django.db.models import Count
import random


def preco_min_max(produtos):
    preco_maximo = 0
    preco_minimo = 0

    if len(produtos) > 0:
        preco_maximo = str(round(list(produtos.aggregate(Max("preco")).values())[0], 2)).replace(',', '.')
        preco_minimo = str(round(list(produtos.aggregate(Min("preco")).values())[0], 2)).replace(',', '.')
        
    return preco_minimo, preco_maximo

def ordenar_produtos(produtos, ordem):
    if ordem == "menor-preco":
        produtos = produtos.order_by("preco")

    elif ordem == "maior-preco":
        produtos = produtos.order_by("-preco")

    elif ordem == "mais-vendidos":
        produtos = produtos.order_by("-quantidade_vendida")

    elif ordem == "adicionados-recentemente":
        produtos = produtos.order_by("-pk")

    elif ordem == "lancamentos":
        produtos = produtos.order_by("-lancamento")

    return produtos

def filtrar(request, produtos):
    dados = request.GET.dict()
    filtro_categorias = request.GET.getlist("categoria")
    filtro_tipos = request.GET.getlist("tipo")
    filtro_plataformas = request.GET.getlist("plataforma")
    filtro_sistemas = request.GET.getlist("sistema")
    filtro_ativacao = request.GET.getlist("ativacao")

    if dados.get("preco_minimo") == None or dados.get("preco_maximo") == None:
        produtos = produtos.filter(preco__gte=0, preco__lte=9999999)
    else:
        produtos = produtos.filter(preco__gte=dados.get("preco_minimo"), preco__lte=dados.get("preco_maximo"))

    if filtro_tipos:
        produtos = produtos.filter(tipo__slug__in=filtro_tipos)

    if filtro_categorias:
        for categoria in filtro_categorias:
            produtos = produtos.filter(categorias__slug=categoria)

    if filtro_plataformas:
        produtos = produtos.filter(sistemas__plataforma__slug__in=filtro_plataformas)

    if filtro_sistemas:
        produtos = produtos.filter(sistemas__slug__in=filtro_sistemas)

    if filtro_ativacao:
        produtos = produtos.filter(ativacao__slug__in=filtro_ativacao)

    return produtos

def context_filtro(produtos):
    catalogo = True 
    filtro_tipos = TipoProduto.objects.all()
    filtro_categorias = Categoria.objects.all()
    filtro_plataformas = Plataforma.objects.all()
    filtro_sistemas = Sistema.objects.all()
    filtro_ativacoes = Ativacao.objects.all()    
    preco_minimo, preco_maximo = preco_min_max(produtos)

    return {"produtos": produtos,
            "catalogo": catalogo, 
            "filtro_tipos": filtro_tipos, 
            "filtro_categorias": filtro_categorias, 
            "filtro_plataformas": filtro_plataformas,
            "filtro_sistemas": filtro_sistemas,
            "filtro_ativacoes": filtro_ativacoes,
            "preco_minimo": preco_minimo,
            "preco_maximo": preco_maximo}

def codigo_aleatorio(len_codigo):
    escolhas_possiveis = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    resultado = ''
    for i in range(len_codigo):
        resultado += random.choice(escolhas_possiveis)
    return resultado