document.addEventListener("DOMContentLoaded", function() {
    var buttons = document.querySelectorAll('#activateModal')
    var buttonActivate = document.getElementById('activateModal')

    buttons.forEach(function(button, index) {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            document.getElementById('confirmationModal').style.display = 'flex';
        });
    
        document.getElementById('confirmButton').addEventListener('click', function(event) {
            if (buttonActivate.href) {
                window.location.href = buttonActivate.href;
            } else {
                var form = document.querySelector('#formModal');
                if (form) {
                    form.submit();
                } 
            }
        });
    
        document.getElementById('cancelButton').addEventListener('click', function() {
            document.getElementById('confirmationModal').style.display = 'none';
        });
    })
});