const fs = require('fs')

fs.ReadFile('../../Data/config.json')


// set default message value
message = document.getElementById('message')
message.innerHTML = ''

// repeat msg update
var msgInterval = window.setInterval(messageUpdate, 120000);
// update message
function messageUpdate() {
    message.innerHTML =
}
