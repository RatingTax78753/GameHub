from django.urls import path, reverse_lazy
from .views import *
from django.contrib.auth import views as auth_view

app_name = 'suporte'

urlpatterns = [
    path('support/', homepage, name="homepage"),
    path('FAQ/topico/<str:slug_topico>/', detalhes_topico, name='detalhes_topico'),
    path('support/pesquisar/', pesquisar_pergunta, name="pesquisar_pergunta"),
    path('support/pergunta/<int:id_pergunta>/', pergunta, name="pergunta"),
    path('support/add/pergunta/', fazer_pergunta, name="fazer_pergunta"),
    path('support/add/feedback/', fazer_feedback, name="fazer_feedback"),
]