from .models import *
from institucional.models import RedesSociais

ATIVACOES_PADRAO = (
    ("Steam", "Steam", "https://store.steampowered.com/login/?redir=account%2Fregisterkey%3Fkey%3DWRREZ-4XWX5-FMGBX&redir_ssl=1"),
    ("Epic", "Epic", "https://www.epicgames.com/help/pt-BR/c-Category_TechnicalSupport/c-TechnicalSupport_GeneralSupport/como-faco-para-resgatar-um-codigo-na-minha-conta-epic-games-a000084732"),
)

CATEGORIAS_PADRAO = (
    ("Ação", "acao", "#8b0000", "Padrao/Categorias/acao.png"),
    ("Anime", "anime", "#008b8b", "Padrao/Categorias/anime.png"),
    ("Aventura", "aventura", "#20b2aa", "Padrao/Categorias/aventura.png"),
    ("Casual", "casual", "#ffa500", "Padrao/Categorias/casual.png"),
    ("Corrida", "corrida", "#ff4500", "Padrao/Categorias/corrida.png"),
    ("Esporte", "esporte", "#008000", "Padrao/Categorias/esporte.png"),
    ("Estratégia", "estrategia", "#800080", "Padrao/Categorias/estrategia.png"),
    ("Luta", "luta", "#800000", "Padrao/Categorias/luta.png"),
    ("Mundo Aberto", "mundo-aberto", "#4682b4", "Padrao/Categorias/mundo-aberto.png"),
    ("Puzzle", "puzzle", "#ff69b4", "Padrao/Categorias/puzzle.png"),
    ("RPG", "rpg", "#800080", "Padrao/Categorias/rpg.png"),
    ("Sci-Fi", "sci-fi", "#00ffff", "Padrao/Categorias/sci-fi.png"),
    ("Simulação", "simulacao", "#ff7f50", "Padrao/Categorias/simulacao.png"),
    ("Sobrevivência", "sobrevivencia", "#db9c00", "Padrao/Categorias/sobrevivencia.png"),
    ("Terror", "terror", "#800080", "Padrao/Categorias/terror.png"),
    ("Visual Novel", "visual-novel", "#ff1493", "Padrao/Categorias/visual-novel.png")
)

DESENVOLVEDORAS_PADRAO = (
    ("Rockstar Games", "Rockstar-Games"),
    ("Bethesda", "Bethesda"),
    ("Creative Assembly", "Creative-Assembly"),
    ("Studio Wildcard", "Studio-Wildcard"),
    ("DICE", "DICE"),
    ("Experiment 101", "Experiment-101"),
    ("Vicarious Visions", "Vicarious-Visions"),
    ("Frontier Developments", "Frontier-Developments"),
    ("Happy Juice Games", "Happy-Juice-Games"),
    ("FromSoftware, Inc.", "FromSoftware-Inc."),
    ("Hello Games", "Hello-Games"),
    ("CyberConnect2 Co. Ltd.", "CyberConnect2-Co-Ltd"),
    ("CAPCOM", "CAPCOM"),
    ("COGNOSPHERE", "COGNOSPHERE")
)

DISTRIBUIDORAS_PADRAO = (
    ("Rockstar Games", "Rockstar-Games"),
    ("Bethesda", "Bethesda"),
    ("SEGA", "SEGA"),
    ("Studio Wildcard", "Studio-Wildcard"),
    ("Eletronic Arts", "Eletronic-Arts"),
    ("THQ Nordic", "THQ-Nordic"),
    ("Activision", "Activision"),
    ("Frontier Developments", "Frontier-Developments"),
    ("Joystick Ventures", "Joystick-Ventures"),
    ("FromSoftware, Inc.", "FromSoftware-Inc."),
    ("Hello Games", "Hello-Games"),
    ("Bandai Namco Entertainment Inc.", "Bandai-Namco-Entertainment-Inc"),
    ("CAPCOM", "CAPCOM"),
    ("COGNOSPHERE", "COGNOSPHERE")
)

FRANQUIAS_PADRAO = (
    ("Red Dead Redemption", "Red-Dead-Redemption"),
    ("Monster Hunter", "Monster-Hunter"),
    ("Fallout", "Fallout"),
    ("Battlefield", "Battlefield"),
    ("Crash", "Crash"),
    ("Dragon Ball", "Dragon-Ball"),
    ("Jurassic World Evolution", "Jurassic-World-Evolution"),
)

GAMEPLAYS_PADRAO = (
    ("Um jogador", "Um-jogador"),
    ("Multijogador", "Multijogador"),
)

PLATAFORAMAS_PADRAO = (
    ("Xbox", "xbox", "#107c10", "Padrao/Plataformas/xbox.png"),
    ("PlayStation", "playstation", "#003791", "Padrao/Plataformas/ps.png"),
    ("PC", "pc", "#000000", "Padrao/Plataformas/pc.png"),
    ("Nintendo", "nintendo", "#e60012", "Padrao/Plataformas/nintendo.png"),
)

SISTEMAS_PADRAO = (
    ("Xbox One", "Xbox-One", 1),
    ("Windows", "Windows", 3),
    ("PS5", "PS5", 2),
    ("Nintendo Switch", "Nintendo-Switch", 8),
)

TIPOSJOGO_PADRAO = (
    ("Jogo", "Jogo", "#0050cb"),
    ("DLC", "DLC", "#7e1bc0"),
    ("Coleção", "Colecao", "#FF6400"),
    ("Pré Venda", "Pre-Venda", "#0099cc"),
)

REDESSOCIAIS_PADRAO = (
    ("Threads",	"https://www.threads.net/?hl=pt-br"),
    ("Discord",	"https://discord.com/channels/@me"),
    ("Instagram",	"https://www.instagram.com/"),
    ("Youtube",	"https://www.youtube.com/"),
    ("Twitch", "https://www.twitch.tv/")
)

def automatic_define(request):
    for ativacao in ATIVACOES_PADRAO:
        nome = ativacao[0]
        slug = ativacao[1]
        link = ativacao[2]
        if not Ativacao.objects.filter(slug=slug).exists():
            Ativacao.objects.create(nome=nome, slug=slug, link= link)

    for categoria in CATEGORIAS_PADRAO:
        nome = categoria[0]
        slug = categoria[1]
        cor = categoria[2]
        imagem = categoria[3]
        if not Categoria.objects.filter(slug=slug).exists():
            Categoria.objects.create(nome=nome, slug=slug, codigo_cor= cor, imagem=imagem)

    for desenvolvedora in DESENVOLVEDORAS_PADRAO:
        nome = desenvolvedora[0]
        slug = desenvolvedora[1]
        if not Desenvolvedora.objects.filter(slug=slug).exists():
            Desenvolvedora.objects.create(nome=nome, slug=slug)

    for distribuidora in DISTRIBUIDORAS_PADRAO:
        nome = distribuidora[0]
        slug = distribuidora[1]
        if not Distribuidora.objects.filter(slug=slug).exists():
            Distribuidora.objects.create(nome=nome, slug=slug)

    for franquias in FRANQUIAS_PADRAO:
        nome = franquias[0]
        slug = franquias[1]
        if not Franquia.objects.filter(slug=slug).exists():
            Franquia.objects.create(nome=nome, slug=slug)

    for gameplay in GAMEPLAYS_PADRAO:
        nome = gameplay[0]
        slug = gameplay[1]
        if not Gameplay.objects.filter(slug=slug).exists():
            Gameplay.objects.create(nome=nome, slug=slug)

    for plataforma in PLATAFORAMAS_PADRAO:
        nome = plataforma[0]
        slug = plataforma[1]
        cor = plataforma[2]
        imagem = plataforma[3]
        if not Plataforma.objects.filter(slug=slug).exists():
            Plataforma.objects.create(nome=nome, slug=slug, codigo_cor= cor, imagem=imagem)

    for sistema in SISTEMAS_PADRAO:
        nome = sistema[0]
        slug = sistema[1]
        plataforma_id = sistema[2]
        if not Sistema.objects.filter(slug=slug).exists():
            plataforma = Plataforma.objects.get(id=plataforma_id)
            Sistema.objects.create(nome=nome, slug=slug, plataforma=plataforma)

    for tipo in TIPOSJOGO_PADRAO:
        nome = tipo[0]
        slug = tipo[1]
        codigo_cor = tipo[2]
        if not TipoProduto.objects.filter(slug=slug).exists():
            TipoProduto.objects.create(nome=nome, slug=slug, codigo_cor=codigo_cor)

    for rede in REDESSOCIAIS_PADRAO:
        nome = rede[0]
        link = rede[1]
        if not RedesSociais.objects.filter(nome=nome).exists():
            RedesSociais.objects.create(nome=nome, link=link)