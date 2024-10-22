const username = document.querySelector('#username').value
const password  = document.querySelector('#password').value
const botao = document.querySelector('#botao')

const user = 'admin'
const senha = 'admin'

botao.addEventListener('click', function(event){ 
    event.preventDefault()
    
    if (username in registros['Username']){
        alert('true')
        
    }else {
        alert('false')
    }

});