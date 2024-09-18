var fixed = document.getElementById("fixed")
var caixa = document.getElementById("caixa")
var button = document.getElementById("button")

button.addEventListener("click", function() {
    fixed.classList.toggle("ativo")
    
    if (fixed.classList.contains("ativo")) {
        button.src = button.getAttribute('data-menos-src')
        button.alt = button.getAttribute('data-menos-alt')
    } else {
        button.src = button.getAttribute('data-mais-src')
        button.alt = button.getAttribute('data-mais-alt')
    }
})