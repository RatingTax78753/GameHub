from django.shortcuts import render

# Create your views here.
def sobre(request):
    return render(request, "institucional/sobre.html")

def termos_uso(request):
    return render(request, "institucional/termos_uso.html")


def politica_privacidade(request):
    return render(request, "institucional/politica_privacidade.html")