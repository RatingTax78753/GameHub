document.addEventListener("DOMContentLoaded", function() {
    var options = document.getElementById("options")
    var imgOptions = document.getElementById("imgOptions")

    if (options && imgOptions) {
        options.addEventListener("click", function () {
        options.classList.toggle("ativo")
    })

    document.addEventListener("click", function(event) {
        if (!options.contains(event.target) && event.target !== imgOptions) {
            options.classList.remove("ativo");
        }
    });}
});