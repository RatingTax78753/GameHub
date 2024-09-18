document.addEventListener("DOMContentLoaded", function() {
    var setaBaixo = document.getElementById("setaInfo");
    var total = document.getElementById("total");
    var infoPreco = document.getElementById("infoPreco");

    total.addEventListener("click", function() {
        if (infoPreco.classList.contains('aberto')) {
            infoPreco.style.maxHeight = 0;
        } else {
            infoPreco.style.maxHeight = infoPreco.scrollHeight + "rem";
        }
        
        setaBaixo.classList.toggle('ativo');
        infoPreco.classList.toggle('aberto');
    });
});