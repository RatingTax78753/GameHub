const radios = document.querySelectorAll('input[name="topico"]');
const textsContext = document.querySelectorAll('label.item-filtrar p');
const filtroSelecionado = document.getElementById('filtroSelecionado')

radios.forEach(function(radio, index) {
    radio.addEventListener("change", function() {
        filtroSelecionado.textContent = textsContext[index].textContent
    })
})
