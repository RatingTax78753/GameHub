document.addEventListener("DOMContentLoaded", function() {
    filter()

    function filter() {
        var filterTriggers = document.querySelectorAll(".filter-trigger");
        var filterContents = document.querySelectorAll(".filter-content");
        var resetFilter = document.getElementById("resetFilter")
        
        filterTriggers.forEach(function(filterTrigger, index) {
            var filterContent = filterContents[index];

            if (filterContent.classList.contains('aberto')) {
                filterContent.style.maxHeight = filterContent.scrollHeight + "rem"; // Corrigido para "px" em vez de "rem"
            } else {
                filterContent.style.maxHeight = 0;
            }

            filterTrigger.addEventListener("click", function() {
                filterTrigger.classList.toggle('ativo')
                filterContent.classList.toggle('aberto');
                
                if (filterContent.classList.contains('aberto')) {
                    filterContent.style.maxHeight = filterContent.scrollHeight + "rem";
                } else {
                    filterContent.style.maxHeight = 0;
                }
            });
        });

        resetFilter.addEventListener("click", function() {
            var currentLocation = window.location;
            var dynamicURL = currentLocation.protocol + "//" + currentLocation.hostname + ":" + currentLocation.port + "/produtos/";
            location.replace(dynamicURL);
        })
    };
});



