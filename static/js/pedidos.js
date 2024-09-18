var pedido = document.querySelectorAll(".pedido");
var detalhesPedidos = document.querySelectorAll(".detalhes-pedido");

pedido.forEach(function(pedido, index) {
    var detalhesPedido = detalhesPedidos[index];

    pedido.addEventListener("click", function() {
        pedido.classList.toggle('ativo')
    })
})


