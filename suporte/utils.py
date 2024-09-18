from django.db.models import Count

def filtrar(produtos, filtro):
    if filtro == "nenhum":
        produtos = produtos
        
    else:
        produtos = produtos.filter(topico__slug=filtro)

    return produtos

def ordenar(produtos, ordem):
    if ordem == "quantidade-respostas":
        produtos = produtos.annotate(num_respostas=Count('respostas')).order_by('-num_respostas')

    elif ordem == "adicionados-recentemente":
        produtos = produtos.order_by("-pk")

    elif ordem == "topicos":
        produtos = produtos.order_by("topico")

    return produtos