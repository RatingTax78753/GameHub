var titulosPerguntas = document.querySelectorAll(".titulo-pergunta")
var perguntas = document.querySelectorAll(".pergunta")

perguntas.forEach(function(pergunta, index) {
    pergunta.addEventListener("mouseover", function() {
        titulosPerguntas[index].classList.add("hover")
    })

    pergunta.addEventListener("mouseout", function() {
        titulosPerguntas[index].classList.remove("hover")
    })
})