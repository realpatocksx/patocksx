document.querySelector('#button').addEventListener('click', verificar)

function verificar() {
    let velocidade = Number(document.querySelector('#vel').value)    
    
    if (velocidade > 60) {
        document.querySelector('#resp').innerHTML = '<strong>DETRAN AVISO!</strong> <br>' + `Voce foi <strong>MULTADO</strong> por esta a ${velocidade}Km/h`
    }
    else if (velocidade < 60) {
        document.querySelector('#resp').innerHTML = '<strong>DETRAN AVISO!</strong> <br>' + 'Parabens voce esta abaixo no limite de 60Km/h'
    }
    else {
        document.querySelector('#resp').innerHTML = '<strong>DETRAN AVISO!</strong> <br>' + 'Voce esta no limite de 60Km/h, para se <strong>MULTADO</strong>. Tenha mais cuidado'
    }
}

