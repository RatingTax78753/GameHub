document.addEventListener("DOMContentLoaded", function() {
    var triggerOrdens = document.getElementById("triggerOrdens")
    var triggerFiltro = document.getElementById("triggerFiltro")
    let filtroSelecionado = null

    if (triggerOrdens) {
        ordenar()
    }

    if (triggerFiltro) {
        filtrar()
    }

    function ordenar() {
        var displaySelecionado = document.getElementById("displaySelecionado")
        var imgOrdemSelecionada = document.getElementById("imgOrdemSelecionada")
        var listOrdens = document.getElementById("listOrdens")
    
        triggerOrdens.addEventListener("click", function() {
            listOrdens.classList.toggle("aberto")
            imgOrdemSelecionada.classList.toggle("ativo")
        })
    
        document.addEventListener("click", function(event) {
            if (!triggerOrdens.contains(event.target)) {
                listOrdens.classList.remove("aberto");
                imgOrdemSelecionada.classList.remove("ativo");
            }
        });
    
    
        var url = new URL(document.URL);
        var ordens = document.getElementsByClassName("item-ordenar");
        const path = window.location.pathname;
        const urlParams = new URLSearchParams(window.location.search);
    
        for (var i = 0; i < ordens.length; i++) {
            url.searchParams.set("ordem", ordens[i].name);
            ordens[i].href = url.href;
        }
    
        if (urlParams.has("ordem")) {
            for (ordem of ordens) {
                if (urlParams.get("ordem") === ordem.name) {
                    displaySelecionado.textContent = ordem.textContent
                }
            }
        } else {
            if (path.includes('mais-populares')) {
                displaySelecionado.textContent = "Mais Vendidos"
            } else if (path.includes('lancamentos')) {
                displaySelecionado.textContent = "Lançamentos"
            } else if (filtroSelecionado) {
                displaySelecionado.textContent = "Quantidade de Respostas"
            } else {
                displaySelecionado.textContent = "Adicionados Recentemente"
            }
        }
    }

    function filtrar() {
        var filtroSelecionado = document.getElementById("filtroSelecionado")
        var imgFiltroSelecionada = document.getElementById("imgFiltroSelecionada")
        var listFiltros = document.getElementById("listFiltros")
    
        triggerFiltro.addEventListener("click", function() {
            listFiltros.classList.toggle("aberto")
            imgFiltroSelecionada.classList.toggle("ativo")
        })
    
        document.addEventListener("click", function(event) {
            if (!triggerFiltro.contains(event.target)) {
                listFiltros.classList.remove("aberto");
                imgFiltroSelecionada.classList.remove("ativo");
            }
        });
    
    
        var url = new URL(document.URL);
        var filtros = document.getElementsByClassName("item-filtrar");
        const urlParams = new URLSearchParams(window.location.search);
    
        for (var i = 0; i < filtros.length; i++) {
            url.searchParams.set("filtro", filtros[i].name);
            filtros[i].href = url.href;
        }
    
        if (urlParams.has("filtro")) {
            for (filtro of filtros) {
                if (urlParams.get("filtro") === filtro.name) {
                    filtroSelecionado.textContent = filtro.textContent
                }
            }
        } else {
            filtroSelecionado.textContent = "----------"
        }
    }
})