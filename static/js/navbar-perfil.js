document.addEventListener("DOMContentLoaded", function() {
    const path = window.location.pathname;
    const links = document.querySelectorAll('.navbar-perfil a');
    const linkPerfil = document.getElementById('linkPerfil');
    const linkListaDesejos = document.getElementById('linkListaDesejos');
    const linkPedidos = document.getElementById('linkPedidos');
    const linkGames = document.getElementById('linkGames');

    for (let link of links) {
        link.classList.remove('selecionado')
    }

    if (path.includes('lista-desejos')) {
        linkListaDesejos.classList.add('selecionado');
    } else if (path.includes('pedidos')) {
        linkPedidos.classList.add('selecionado');
    } else if (path.includes('games')) {
        linkGames.classList.add('selecionado');
    } else {
        linkPerfil.classList.add('selecionado');
    }
});