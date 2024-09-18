document.addEventListener("DOMContentLoaded", function() {
    var produtos = document.querySelectorAll(".produto")
    var divsChaveAtivacao = document.querySelectorAll(".chave-produto")

    produtos.forEach(function(produto, index) {
        produto.addEventListener("click", function() {
            for (let chave of divsChaveAtivacao) {
                if (chave !== divsChaveAtivacao[index]) {
                    chave.classList.remove('aberto');
                }
            }

            divsChaveAtivacao[index].classList.toggle('aberto');
    });})

    var buttonsUnlockKey = document.querySelectorAll(".unlock-key");
    var imgsUnlockKey = document.querySelectorAll(".unlock-key img");

    buttonsUnlockKey.forEach(function(buttonUnlockKey, index) {
        buttonUnlockKey.addEventListener("mouseover", function() {
            var unlockSrc = imgsUnlockKey[index].getAttribute('data-unlock-src');
            imgsUnlockKey[index].src = unlockSrc;
            imgsUnlockKey[index].alt = "Img cadeado destrancado";
        });

        buttonUnlockKey.addEventListener("mouseout", function() {
            var lockSrc = imgsUnlockKey[index].getAttribute('data-lock-src');
            imgsUnlockKey[index].src = lockSrc;
            imgsUnlockKey[index].alt = "Img cadeado trancado";
        });
    });

})
