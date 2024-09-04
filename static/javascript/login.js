const signUpButton = document.getElementById('SignUp');
const signInButton = document.getElementById('SignIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
    container.classList.add('right-panel-active');
});

signInButton.addEventListener('click', () => {
    container.classList.remove('right-panel-active');
});

document.addEventListener('DOMContentLoaded', function() {
    var messages = document.querySelectorAll('.fade-in'); // Note the plural form
    
    messages.forEach(function(message) {
        setTimeout(function() {
            message.classList.remove('fade-in');
            message.classList.add('fade-out');
        }, 900); // Adjust the delay as needed (in milliseconds)
    });
});
