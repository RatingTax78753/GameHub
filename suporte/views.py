import django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *
from .utils import *
# Create your views here.

def homepage(request):
    todos_topicos = Topico.objects.all()
    todos_topicos = [todos_topicos[i:i + 4] for i in range(0, len(todos_topicos), 4)]
    homepage = True
    context = {"todos_topicos": todos_topicos, "homepage": homepage}
    return render(request, "suporte/homepage.html", context)

def detalhes_topico(request, slug_topico):
    topico = Topico.objects.get(slug=slug_topico)
    context = {'topico': topico}
    return render(request, 'suporte/detalhes_topico.html', context)


def pesquisar_pergunta(request):
    if request.method == "GET":
        pagina_pesquisa = True
        topicos = Topico.objects.all()

        dados = request.GET.dict()
        termo_pesquisa = dados.get("support_query")

        if termo_pesquisa:
            resultados = Pergunta.objects.filter(titulo__icontains=termo_pesquisa)
        else:
            resultados = Pergunta.objects.all()


        ordem = request.GET.get("ordem", "quantidade-respostas")
        resultados = ordenar(resultados, ordem)

        filtro = request.GET.get("filtro", "nenhum")
        resultados = filtrar(resultados, filtro)
        
    context = {"termo_pesquisa": termo_pesquisa, "resultados": resultados, "topicos": topicos, "pagina_pesquisa": pagina_pesquisa}
    return render(request, "suporte/pesquisar.html", context)


def pergunta(request, id_pergunta):
    pergunta = Pergunta.objects.get(id=id_pergunta)

    if request.method == "POST" and request.user.is_authenticated:
        dados = request.POST.dict()
        resposta = dados.get("resposta")

        Resposta.objects.create(
            pergunta=pergunta,
            resposta=resposta,
            autor = request.user,
            data = django.utils.timezone.now()
        )
        
        return redirect("suporte:pergunta", pergunta.id)
    
    context = {"pergunta": pergunta}
    return render(request, "suporte/pergunta.html", context)

@login_required
def fazer_pergunta(request):
    erro = None
    topicos = Topico.objects.all()

    if request.method == "POST":
        dados = request.POST.dict()

        if "titulo" in dados and "conteudo" in dados:
            titulo = dados.get("titulo")
            conteudo = dados.get("conteudo")
            topico_slug = dados.get("topico")

            if titulo != "" and conteudo != "":
                if topico_slug and topico_slug != "":
                    topico = Topico.objects.get(slug=topico_slug)  

                    pergunta = Pergunta.objects.create(
                                topico =topico,
                                titulo = titulo,
                                pergunta = conteudo,
                                autor = request.user,
                                data = django.utils.timezone.now())
                    
                    return redirect("suporte:pergunta", pergunta.id)
                else:
                    erro = "topico" 
            else:
                erro = "preenchimento"
        else:
            erro = "preenchimento"

    context = {"topicos": topicos, "erro": erro}
    return render(request, "suporte/forms/fazer_pergunta.html", context)

@login_required
def fazer_feedback(request):
    erro = False

    notas = []
    for nota in NOTAS:
        notas.append(nota[1])

    if request.method == "POST":
        dados = request.POST.dict()

        if "nota" in dados:
            nota = dados.get("nota")

            if nota != "":
                if "motivo" in dados:
                    motivo = dados.get("motivo")

                    Feedback.objects.create(
                        nota=nota,
                        motivo=motivo,
                        autor = request.user,
                        data = django.utils.timezone.now())
                     
                    return redirect("suporte:homepage")
                
                else:
                    Feedback.objects.create(
                        nota=nota,
                        autor = request.user,
                        data = django.utils.timezone.now())
                     
                    return redirect("suporte:homepage")
            else:
                erro = True
        else:
            erro = True
    context = {"notas": notas, "erro": erro}
    return render(request, "suporte/forms/fazer_feedback.html", context)