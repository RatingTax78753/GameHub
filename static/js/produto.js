document.addEventListener("DOMContentLoaded", function() {
    var linkImgProdutos = document.querySelectorAll(".link-img-produto");
    var divImgInfoProdutos = document.querySelectorAll(".div-img-info");
    var buttonListaDesejos = document.querySelectorAll(".button-lista-desejos")
    
    linkImgProdutos.forEach(function(linkImgProdutos, index) {
        linkImgProdutos.addEventListener("mouseover", function() {
            divImgInfoProdutos[index].classList.add('ativo');
            buttonListaDesejos[index].classList.add('ativo');
        });
        linkImgProdutos.addEventListener("mouseout", function() {
            divImgInfoProdutos[index].classList.remove('ativo');
            buttonListaDesejos[index].classList.remove('ativo');
        });
    });
});