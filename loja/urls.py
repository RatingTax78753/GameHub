from django.contrib.auth import views
from django.urls import path
from .views import *

app_name = 'loja'

urlpatterns = [
    path('', homepage, name="homepage"),

    path('produtos/', todos_produtos, name="todos_produtos"),
    path('produtos/mais-populares/', mais_populares, name="mais_populares"),
    path('produtos/lancamentos/', lancamentos, name="lancamentos"),
    path('produtos/gratuitos/', gratuito, name="gratuito"),

    path('detalhes/<str:slug_produto>/', detalhes_produto, name="detalhes_produto"),

    path('pesquisar/', pesquisar, name="pesquisar"),

    path('categorias/', todas_categorias, name="todas_categorias"),
    path('categoria/<str:slug_categoria>', produtos_por_categoria, name="produtos_por_categoria"),

    path('plataforma/<str:slug_plataforma>/', produtos_por_plataformas, name="produtos_por_plataformas"),
    path('plataforma/<str:slug_plataforma>/sistema/<str:slug_sistema>', produtos_por_sistema, name="produtos_por_sistema"),

    path('carrinho/', carrinho, name="carrinho"),
    path('carrinho/adicionar/<int:id_produto>/', adicionar_carrinho, name="adicionar_carrinho"),
    path('carrinho/remover/<int:id_produto>/', remover_carrinho, name="remover_carrinho"),

    path('finalizar/pedido/<int:id_pedido>/', finalizar_compra, name="finalizar_compra"),
    path('finalizar/pagamento/', finalizar_pagamento, name="finalizar_pagamento"),
    
    path('perfil/<str:nome_usuario>/', perfil, name="perfil"),
    path('perfil/<str:nome_usuario>/lista-desejos/', lista_desejos, name="lista_desejos"),
    path('perfil/<str:nome_usuario>/pedidos/', pedidos, name="pedidos"),
    path('perfil/<str:nome_usuario>/games/', games, name="games"),

    path('perfil/<str:nome_usuario>/editar/', editar_perfil, name="editar_perfil"),
    path('perfil/<str:nome_usuario>/senha/mudar/', mudar_senha, name="mudar_senha"),
    path('perfil/<str:nome_usuario>/excluir/', excluir_conta, name="excluir_conta"),

    path('listadesejos/adicionar/<int:id_produto>/', adicionar_lista_desejos, name="adicionar_lista_desejos"),
    path('listadesejos/remover/<int:id_produto>/', remover_lista_desejos, name="remover_lista_desejos"),
    path('perfil/<str:nome_usuario>/games/<int:id_item_pedido>/liberar-chave', liberar_chave, name="liberar_chave"),

    path('login/', fazer_login, name="fazer_login"),
    path('criarconta/', criar_conta, name="criar_conta"),
    path('logout/', fazer_logout, name="fazer_logout"),
    
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]