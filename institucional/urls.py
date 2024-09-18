from django.urls import path
from .views import *

app_name = 'institucional'

urlpatterns = [
    path('sobre/', sobre, name="sobre"),
    path('termos-de-uso/', termos_uso, name="termos_uso"),
    path('politica-de-privacidade/', politica_privacidade, name="politica_privacidade"),
]