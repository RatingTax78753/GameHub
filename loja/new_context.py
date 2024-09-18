from .models import *
from institucional.models import *

def context_navbar(request):
    plataformas_navbar = Plataforma.objects.all()
    redes_sociais_footer = RedesSociais.objects.all()

    context = {"plataformas_navbar": plataformas_navbar, "redes_sociais_footer": redes_sociais_footer}
    return context

def carrinho(request):
    qnt_produtos_carrinho = 0
    if request.user.is_authenticated:
        cliente = request.user.cliente
    else:
        return {"qnt_produtos_carrinho": 0}

    pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False)
    itens_pedido = ItensPedido.objects.filter(pedido=pedido)
    for item in itens_pedido:
        qnt_produtos_carrinho += 1
    return {"qnt_produtos_carrinho": qnt_produtos_carrinho}
