const radios = document.querySelectorAll('input[name="nota"]');
const labels = document.querySelectorAll(".nota-feedback label")
const estrelaCheia = '../../../static/images/estrela-cheia.png'
const estrelaVazia = '../../../static/images/estrela-vazia.svg'

radios.forEach(function(radio) {
    radio.addEventListener("change", function() {
        const valor = parseInt(radio.value);

        labels.forEach((label, index) => {
            if (index < valor) {
                label.style.backgroundImage = `url('${estrelaCheia}')`
            } else {
                label.style.backgroundImage = `url('${estrelaVazia}')`
            }
        });
    });
});