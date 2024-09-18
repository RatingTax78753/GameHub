const textarea = document.getElementById('resposta');
const minHeight = parseFloat(window.getComputedStyle(textarea).minHeight);
const botoes = document.querySelector(".botoes")

textarea.addEventListener('input', function() {
    const scrollHeight = this.scrollHeight;
    const charCount = this.value.length;

    if (scrollHeight > 48 && charCount > 50) {
        this.style.height = `${scrollHeight}px`; 
    } else {
        this.style.height = `${minHeight}px`
    }
});

textarea.addEventListener('click', function() {
    botoes.classList.add("ativo")
})

document.addEventListener('click', function(event) {
    if (!textarea.contains(event.target) && !botoes.contains(event.target)) {
        if (textarea.value.trim() === "") {  
            botoes.classList.remove("ativo");
        }
    }
});