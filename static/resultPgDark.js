'use strict'
const switcher = document.querySelector('.back_home');
var mode = "dark-theme"
switcher.addEventListener('click', function () {
    location.replace("http://127.0.0.1:5000/Dark")
});