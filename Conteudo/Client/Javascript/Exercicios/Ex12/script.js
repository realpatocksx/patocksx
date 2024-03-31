function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var resp = document.querySelector('.resp')
    var txtano = document.querySelector('#txtano')

    if (txtano,value.length == 0 || txtano.value > ano) {
        alert('Voce nao colocou a sua idade de nascimento ou colocou maior que o ano atual')
    }else {
        alert('Colocou tudo certinho')
    }
        
}