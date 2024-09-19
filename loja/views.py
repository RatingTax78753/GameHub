from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import django
import django.utils
from .api_mercadopago import *
from .models import *
from .utils import *
from .automatic import *

# Create your views here.
def homepage(request):
    automatic_define(request)

    produtos_slider = Produto.objects.filter(ativo=True, estoque_produto__quantidade__gte=0).order_by('?')[:4]
    
    produtos_mais_vendidos = Produto.objects.filter(ativo=True, estoque_produto__quantidade__gte=0).order_by('-quantidade_vendida')[:12]
    
    produtos_adicinados_recentemente = Produto.objects.filter(ativo=True, estoque_produto__quantidade__gte=0).order_by('-id')[:12]
    
    categorias_carousel = list(Categoria.objects.order_by("?")[:12])
    categorias_carousel.sort(key=lambda x: x.slug)

    desenvolvedora = Desenvolvedora.objects.order_by("?").first()
    produtos_desenvolvedora = Produto.objects.filter(ativo=True, estoque_produto__quantidade__gte=0, desenvolvedora=desenvolvedora.id)[:12]

    while len(produtos_desenvolvedora) == 0:
        desenvolvedora = Desenvolvedora.objects.order_by("?").first()
        produtos_desenvolvedora = Produto.objects.filter(ativo=True, estoque_produto__quantidade__gte=0, desenvolvedora=desenvolvedora.id)[:12]
    
    categoria = Categoria.objects.order_by('?').first()
    produtos_categoria = Produto.objects.filter(ativo=True, estoque_produto__quantidade__gte=0, categorias=categoria)[:12]

    plataformas_carousel = list(Plataforma.objects.order_by("id")[:4])
    plataformas_carousel.sort(key=lambda x: x.slug)

    context = {"produtos_slider": produtos_slider, 
               "produtos_mais_vendidos": produtos_mais_vendidos, 
               "produtos_adicinados_recentemente": produtos_adicinados_recentemente,
               "categorias_carousel": categorias_carousel, 
               "desenvolvedora": desenvolvedora,
               "produtos_desenvolvedora": produtos_desenvolvedora, 
               "categoria": categoria,
               "produtos_categoria": produtos_categoria,
               "plataformas_carousel": plataformas_carousel}

    return render(request, 'loja/homepage.html', context)



def todos_produtos(request):
    produtos = Produto.objects.filter(ativo=True, estoque_produto__quantidade__gte=0)

    if request.method == "GET":
        produtos = filtrar(request, produtos)
            
    ordem = request.GET.get("ordem", "adicionado-recentemente")
    produtos = ordenar_produtos(produtos, ordem)

    context = context_filtro(produtos)
    return render(request, 'loja/Produtos/catalogo.html', context)

def mais_populares(request):
    produtos = Produto.objects.filter(ativo=True, estoque_produto__quantidade__gte=0)
    pagina = "Mais populares"

    if request.method == "GET":
        produtos = filtrar(request, produtos)
            
    ordem = request.GET.get("ordem", "mais-vendidos")
    produtos = ordenar_produtos(produtos, ordem)

    context = context_filtro(produtos)
    context.update({"pagina": pagina})
    return render(request, 'loja/Produtos/catalogo.html', context)

def lancamentos(request):
    produtos = Produto.objects.filter(ativo=True, estoque_produto__quantidade__gte=0)
    pagina = "Lançamentos"    

    if request.method == "GET":
        produtos = filtrar(request, produtos)
            
    ordem = request.GET.get("ordem", "lancamentos")
    produtos = ordenar_produtos(produtos, ordem)

    context = context_filtro(produtos)
    context.update({"pagina": pagina})
    return render(request, 'loja/Produtos/catalogo.html', context)

def gratuito(request):
    produtos = Produto.objects.filter(ativo=True, estoque_produto__quantidade__gte=0, preco=0)
    pagina = "Gratuitos"

    if request.method == "GET":
        produtos = filtrar(request, produtos)
            
    ordem = request.GET.get("ordem", "adicionado-recentemente")
    produtos = ordenar_produtos(produtos, ordem)

    context = context_filtro(produtos)
    context.update({"pagina": pagina})    
    return render(request, 'loja/Produtos/catalogo.html', context)


def detalhes_produto(request, slug_produto):
    produto = Produto.objects.get(slug=slug_produto)
    itens_carrinho = []

    if request.user.is_authenticated:
        cliente = request.user.cliente
        pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False)
        itens_pedido = ItensPedido.objects.filter(pedido=pedido)
        for item in itens_pedido:
            itens_carrinho.append(item.estoque_produto.produto)

    context = {"produto": produto, "itens_carrinho":itens_carrinho}
    return render(request, 'loja/Produtos/detalhes_produto.html', context)


def pesquisar(request):
    if request.method == "GET":
        dados = request.GET.dict()
        termo_pesquisa = dados.get("query")
        pagina = f'Pesquisa: "{termo_pesquisa}"'

        if termo_pesquisa:
            resultados = Produto.objects.filter(ativo=True, estoque_produto__quantidade__gte=0, nome__icontains=termo_pesquisa)
        else:
            resultados = Produto.objects.filter(ativo=True, estoque_produto__quantidade__gte=0)

        resultados = filtrar(request, resultados)
                
        ordem = request.GET.get("ordem", "adicionado-recentemente")
        resultados = ordenar_produtos(resultados, ordem)
        
    context = context_filtro(resultados)
    context.update({"termo_pesquisa": termo_pesquisa, "produtos": resultados, "pagina": pagina})
    return render(request, "loja/Produtos/catalogo.html", context)



def todas_categorias(request):
    categorias = Categoria.objects.all()
    grupos_categorias = [categorias[i:i + 4] for i in range(0, len(categorias), 4)]
    context = {"grupos_categorias": grupos_categorias}
    return render(request, 'loja/categorias.html', context)

def produtos_por_categoria(request, slug_categoria=None):
    produtos = Produto.objects.filter(ativo=True, estoque_produto__quantidade__gte=0)

    if slug_categoria:
        produtos = produtos.filter(categorias__slug=slug_categoria)

    if request.method == "GET":
        produtos = filtrar(request, produtos)
            
    ordem = request.GET.get("ordem", "adicionado-recentemente")
    produtos = ordenar_produtos(produtos, ordem)

    context = context_filtro(produtos)
    return render(request, 'loja/Produtos/catalogo.html', context)



def produtos_por_plataformas(request, slug_plataforma=None):
    produtos = Produto.objects.filter(ativo=True, estoque_produto__quantidade__gte=0)
    if slug_plataforma:
        produtos = produtos.filter(sistemas__plataforma__slug=slug_plataforma)

    if request.method == "GET":
        produtos = filtrar(request, produtos)
            
    ordem = request.GET.get("ordem", "adicionado-recentemente")
    produtos = ordenar_produtos(produtos, ordem)

    context = context_filtro(produtos)
    return render(request, 'loja/Produtos/catalogo.html', context)

def produtos_por_sistema(request, slug_sistema=None, slug_plataforma=None):
    produtos = Produto.objects.filter(ativo=True, estoque_produto__quantidade__gte=0)
    if slug_sistema:
        produtos = produtos.filter(sistemas__plataforma__slug=slug_plataforma)
        produtos = produtos.filter(sistemas__slug=slug_sistema)

    if request.method == "GET":
        produtos = filtrar(request, produtos)
            
    ordem = request.GET.get("ordem", "adicionado-recentemente")
    produtos = ordenar_produtos(produtos, ordem)

    context = context_filtro(produtos)
    return render(request, 'loja/Produtos/catalogo.html', context)




@login_required
def carrinho(request):
    if request.user.is_authenticated:
        cliente = request.user.cliente

    pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False)
    itens_pedido = ItensPedido.objects.filter(pedido=pedido)
    context = {"itens_pedido": itens_pedido, "pedido": pedido}
    return render(request, 'loja/carrinho.html', context)

def adicionar_carrinho(request, id_produto):
    if request.method == "POST" and id_produto:
        resposta = redirect("loja:carrinho")
        if request.user.is_authenticated:
            cliente = request.user.cliente
            pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False)
            estoque_produto = EstoqueProduto.objects.get(produto__id=id_produto)
            item_pedido, criado = ItensPedido.objects.get_or_create(estoque_produto=estoque_produto, pedido=pedido)
            item_pedido.no_carrinho = True
            pedido.data_finalizacao = django.utils.timezone.now()

            if pedido.codigo_transacao == None:
                pedido.codigo_transacao = f"#{codigo_aleatorio(15)}"

            pedido.save()
            item_pedido.save()
            return resposta
    else:
        return redirect("loja:detalhes_produto", id_produto=id_produto)
       
def remover_carrinho(request, id_produto):
    if request.method == "POST" and id_produto:
        resposta = redirect("loja:carrinho")
        if request.user.is_authenticated:
            cliente = request.user.cliente
            pedido, criado = Pedido.objects.get_or_create(cliente=cliente, finalizado=False)
            estoque_produto = EstoqueProduto.objects.get(produto__id=id_produto)
            item_pedido, criado = ItensPedido.objects.get_or_create(estoque_produto=estoque_produto, pedido=pedido)
            pedido.data_finalizacao = django.utils.timezone.now()

            pedido.save()
            item_pedido.delete()
            return resposta
    else:
        return redirect("loja:detalhes_produto", id_produto=id_produto)



@login_required
def finalizar_compra(request, id_pedido):
    erro = None

    if request.method == "POST":
        dados = request.POST.dict()
        total = dados.get("total")
        total = float(total.replace(",", "."))
        pedido = Pedido.objects.get(id=id_pedido)

        if total > 0:
            if total != float(pedido.preco_total):
                erro = "preco"
            
            if request.user.is_authenticated:
                pagamento_existente = Pagamento.objects.filter(pedido=pedido, aprovado=False).first()
                
                if pagamento_existente:
                    link_pagamento = pagamento_existente.link_pagamento
                    return redirect(link_pagamento)
                
                else:
                    itens_pedido = ItensPedido.objects.filter(pedido=pedido)

                    link = request.build_absolute_uri(reverse("loja:finalizar_pagamento"))
                    link_pagamento, id_pagamento = criar_pagamento(itens_pedido, link)

                    pagamento = Pagamento.objects.create(id_pagamento=id_pagamento, pedido=pedido, link_pagamento=link_pagamento)
                    pagamento.save()

                    return redirect(link_pagamento)
        else:
            pedido.finalizado = True
            pedido.save()

            return redirect("loja:games", request.user.username)
            
    else:
        return redirect("loja:games", request.user.username)

def finalizar_pagamento(request):
    dados = request.GET.dict()

    status = dados.get("status")
    id_pagamento = dados.get("preference_id")

    if not status or not id_pagamento:
        return redirect("loja:carrinho")

    if dados.get("payment_id"):
        metodo, preco_final = info_pedido(dados.get("payment_id"))

    if status == "approved":
        pagamento = Pagamento.objects.get(id_pagamento=id_pagamento)
        pagamento.aprovado = True

        if metodo == "credit_card":
            metodo = "Cartão de crédito"

        elif metodo == "account_money":
            metodo = "Saldo em conta"

        elif metodo == "debit_card":
            metodo = "Cartão de débito"

        elif metodo == "ticket":
            metodo = "Boleto"
            
        else:
            metodo = metodo

        pagamento.metodo = metodo

        pedido = pagamento.pedido
        pedido.preco_final = preco_final
        pedido.finalizado = True
        pedido.data_finalizacao = django.utils.timezone.now()

        pedido.save()
        pagamento.save()

        return redirect("loja:games", request.user.username)
    else:
        return redirect("loja:carrinho")



@login_required
def perfil(request, nome_usuario):
    if request.user.is_authenticated:
        if nome_usuario == request.user.username:
            cliente = Cliente.objects.get(usuario__username=nome_usuario)
            context = {"cliente": cliente}
        else:
            return redirect("loja:perfil", nome_usuario=request.user.username)
        return render(request, "loja/Perfil/perfil.html", context)

@login_required
def pedidos(request, nome_usuario):
    if request.user.is_authenticated:
        if nome_usuario == request.user.username:
            usuario = User.objects.get(username=nome_usuario)
            pedidos = Pedido.objects.filter(cliente=usuario.cliente).order_by("-data_finalizacao")

            pedidos_filtrados = []
            for pedido in pedidos:
                if len(pedido.itens_pedido.all()) > 0:
                    pedidos_filtrados.append(pedido)

            context = {"pedidos": pedidos_filtrados}
        else:
            return redirect("loja:pedidos", nome_usuario=request.user.username)
        return render(request, "loja/Perfil/pedidos.html", context)
    
@login_required
def lista_desejos(request, nome_usuario):
    if request.user.is_authenticated:
        if nome_usuario == request.user.username:
            cliente = Cliente.objects.get(usuario__username=nome_usuario)
            lista_desejos = cliente.lista_desejos.all().order_by("slug")

            user_cliente = request.user.cliente
            pedido, criado = Pedido.objects.get_or_create(cliente=user_cliente, finalizado=False)
            itens_pedido = ItensPedido.objects.filter(pedido=pedido)

            itens_carrinho = []
            for item in itens_pedido:
                itens_carrinho.append(item.estoque_produto.produto)

            context = {"lista_desejos": lista_desejos, "itens_carrinho": itens_carrinho}
        else:
            return redirect("loja:lista_desejos", nome_usuario=request.user.username)
        return render(request, "loja/Perfil/lista_desejos.html", context)
    
@login_required
def games(request, nome_usuario):
    if request.user.is_authenticated:
        if nome_usuario == request.user.username:
            cliente = request.user.cliente
            pedidos = Pedido.objects.filter(cliente=cliente, finalizado=True).order_by("-id")

            produtos = []
            for pedido in pedidos:
                itens_pedido = ItensPedido.objects.filter(pedido=pedido)

                for item_pedido in itens_pedido:
                    produto = item_pedido.estoque_produto.produto
                    pedido = item_pedido.pedido
                    if Chave.objects.filter(itens_pedido=item_pedido):
                        chave = Chave.objects.get(itens_pedido=item_pedido)
                    else:
                        chave = "A"

                    produtos.append({'produto': produto, 'pedido': pedido, 'chave': chave, "item_pedido": item_pedido})

            context = {"produtos": produtos}
        else:
            return redirect("loja:games", nome_usuario=request.user.username)
        return render(request, "loja/Perfil/games.html", context)
    


@login_required
def editar_perfil(request, nome_usuario):
    erro = ""
    
    if request.user.is_authenticated:
        if nome_usuario == request.user.username:
            cliente = Cliente.objects.get(usuario__username=nome_usuario)

            if request.method == "POST":
                dados = request.POST.dict()
                imagem = request.FILES.dict()

                if "username" in dados and "email" in dados:
                    username = dados.get("username")
                    email = dados.get("email")

                    if email == "" or username == "":
                        erro = "preenchimento"

                    if "foto-perfil" in imagem:
                        foto_perfil = imagem.get("foto-perfil")
                    else:
                        foto_perfil = request.user.cliente.foto_perfil

                    if username != request.user.username:
                        check_username = User.objects.filter(username=username)

                        if len(check_username) > 0:
                            erro = "username_indisponivel"

                    if email != request.user.email:
                        check_email = User.objects.filter(email=email)

                        if len(check_email) > 0:
                            erro = "email_indisponivel"

                    if "telefone" in dados:
                        telefone = dados.get("telefone")

                        if telefone != request.user.cliente.telefone:
                            check_telefone = Cliente.objects.filter(telefone=telefone)

                            if len(check_telefone) > 0:
                                erro = "telefone_indisponivel"
                    else:
                        telefone = ""

                    if not erro:
                        request.user.cliente.foto_perfil = foto_perfil 
                        request.user.username = username
                        request.user.email = email
                        request.user.cliente.telefone = telefone 
                        request.user.save()
                        request.user.cliente.save()
                        return redirect("loja:perfil", nome_usuario=request.user.username)
                else:
                    erro = "preenchimento"
        else:
            return redirect("loja:editar_perfil", nome_usuario=request.user.username)

    context = {"cliente": cliente, "erro": erro}
    return render(request, "loja/Perfil/Forms/editar_perfil.html", context)

@login_required
def mudar_senha(request, nome_usuario):
    erro = ""

    if request.user.is_authenticated:
        if nome_usuario == request.user.username:
            cliente = Cliente.objects.get(usuario__username=nome_usuario)
            context = {"cliente": cliente}
        else:
            return redirect("loja:mudar_senha", nome_usuario=request.user.username)

    if request.method == "POST":
        dados = request.POST.dict()

        if "senha_atual" in dados:
            senha_atual = dados.get("senha_atual")
            senha_nova = dados.get("senha_nova")
            confirmacao_senha_nova = dados.get("confirmacao_senha_nova")

            if senha_nova != "" and confirmacao_senha_nova != "":
                if senha_nova == confirmacao_senha_nova:
                    usuario = authenticate(request, username=request.user.username, password=senha_atual)
                    if usuario:
                        usuario.set_password(senha_nova)
                        usuario.save()
                        
                        return redirect("loja:fazer_login")
                    else:
                        erro = "senha_incorreta"
                else:
                    erro = "senhas_diferentes"
            else:
                erro = "preenchimento"

    context = {"erro": erro}
    return render(request, "loja/Perfil/Forms/mudar_senha.html", context)

@login_required
def excluir_conta(request, nome_usuario):
    erro = ""
    
    if request.user.is_authenticated:
        if nome_usuario == request.user.username:
            if request.method == "POST":
                dados = request.POST.dict()
                senha = dados.get("senha")

                if senha != "" and "senha" in dados:
                    usuario = authenticate(request, username=request.user.username, password=senha)

                    if usuario:
                        usuario.delete()
                        return redirect("loja:homepage")
                    else:
                        erro = "senha_incorreta"
                else:
                    erro = "preenchimento"  
        else:
            return redirect("loja:excluir_conta", nome_usuario=request.user.username)
        
        context = {"erro": erro}
    return render(request, "loja/Perfil/Forms/excluir_conta.html", context)



@login_required
def adicionar_lista_desejos(request, id_produto):
    if request.method == "POST" and id_produto:
        if request.user.is_authenticated:
            cliente = request.user.cliente
            produto = Produto.objects.get(id=id_produto)
            cliente.lista_desejos.add(produto)
            cliente.save()
            
        return redirect('loja:lista_desejos', nome_usuario=request.user.username)
    else:
        return redirect('loja:todos_produtos')
    
@login_required
def remover_lista_desejos(request, id_produto):
    if request.method == "POST" and id_produto:
        if request.user.is_authenticated:
            cliente = request.user.cliente
            produto = Produto.objects.get(id=id_produto)
            cliente.lista_desejos.remove(produto)
            cliente.save()

        return redirect('loja:lista_desejos', nome_usuario=request.user.username)
    else:
        return redirect('loja:todos_produtos')
    
@login_required
def liberar_chave(request, nome_usuario, id_item_pedido):
    if request.user.is_authenticated:
        item = ItensPedido.objects.get(id=id_item_pedido)
        chaves_disponiveis = Chave.objects.filter(produto=item.estoque_produto.produto, itens_pedido__isnull=True)

        if item.chave_liberada == True:
            item.chave_liberada = False
        else:
            item.chave_liberada = True

        if not item.chave and chaves_disponiveis.exists():
            chave_aleatoria = random.choice(chaves_disponiveis)
            item.chave = chave_aleatoria
            item.chave_liberada = True
            chave_aleatoria.item = item
            chave_aleatoria.save()

        item.save()
        return redirect("loja:games", nome_usuario=request.user.username)



def fazer_login(request):
    erro = ""

    if request.user.is_authenticated:
        return redirect("loja:perfil", request.user.username)
    
    if request.method == "POST":
        dados = request.POST.dict()

        if "campo" in dados and "senha" in dados:
            campo = dados.get("campo")
            senha = dados.get("senha")

            if campo == "" or senha == "":
                erro = "preenchimento"

            usuario = authenticate(request, username=campo, password=senha)

            if usuario:
                login(request, usuario)
                return redirect("loja:perfil", request.user.username)
            else:
                try:
                    username = User.objects.get(email=campo)
                    usuario = authenticate(request, username=username, password=senha)
                except User.DoesNotExist:
                    erro = "inexistente"

                if usuario:
                    login(request, usuario)
                    return redirect("loja:perfil", request.user.username)
                else:
                    erro = "inexistente"
        else:
            erro = "preenchimento"
    context = {"erro": erro}
    return render(request, "loja/Perfil/Forms/fazer_login.html", context)

def criar_conta(request):
    erro = ""

    if request.user.is_authenticated:
        return redirect("loja:perfil", request.user.username)

    if request.method == "POST":
            dados = request.POST.dict()
            print(dados)

            if "email" in dados and "senha" in dados and "confirmacao_senha" in dados:
                email = dados.get("email")
                senha = dados.get("senha")
                confirmacao_senha = dados.get("confirmacao_senha")
                
                if email != "" and senha != "" and confirmacao_senha != "":
                    try:
                        validate_email(email)
                    except ValidationError:
                        erro = "email_invalido"

                    if senha == confirmacao_senha:
                        usuario, criado = User.objects.get_or_create(username=email ,email=email)

                        if not criado:
                            erro = "usuario_existente"
                        else:
                            usuario.set_password(senha)
                            usuario.save()

                            username = User.objects.get(email=email)
                            usuario = authenticate(request, username=username, password=senha)
                            login(request, usuario)

                            cliente, criado = Cliente.objects.get_or_create(usuario=usuario)
                            cliente.usuario = usuario
                            cliente.save()
                            return redirect("loja:perfil", request.user.username)
                    else:
                        erro = "senhas_diferentes"
                else:
                    erro = "preenchimento"
            
    context = {"erro": erro}
    return render(request, "loja/Perfil/Forms/criar_conta.html", context)

@login_required
def fazer_logout(request):
    logout(request)
    return redirect("loja:homepage")
