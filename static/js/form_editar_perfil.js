document.addEventListener("DOMContentLoaded", function() {
    var fotoPerfil = document.getElementById("fotoPerfil");
    var divAlterarFotoPerfil = document.getElementById("divAlterarFotoPerfil");

    fotoPerfil.addEventListener("mouseover", function () {
        divAlterarFotoPerfil.classList.add("ativo")
    })

    fotoPerfil.addEventListener("mouseout", function () {
        divAlterarFotoPerfil.classList.remove("ativo")
    })
});

function previewImage(event) {
    var input = event.target;
    var reader = new FileReader();
    reader.onload = function(){
        var fotoPerfil = document.getElementById('fotoPerfil');
        
        if (fotoPerfil) {
            fotoPerfil.src = reader.result;
        }
    };
    reader.readAsDataURL(input.files[0]);
}