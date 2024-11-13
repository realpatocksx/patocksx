dados = {
    '17999241788': {
        'Nome': 'Pedro Henrique Castro',
        'Cpf': 17999241788,
        'Nascimento': '25/02/2008',
        'Cidade': 'Vila Velha - ES'
    },

    '98765432100': {
        'Nome': 'Joao Victor Mendes da Silva',
        'Cpf': 98765432100,
        'Nascimento': '17/09/1992',
        'Cidade': 'Perino - ES'
    },

    '68769932151': {
        'Nome': 'Maria Ferdinandes Aparecida',
        'Cpf': 68769932151,
        'Nascimento': '29/11/1965',
        'Cidade': 'Avenida Braga - MG'
    },

    '87765432198': {
        'Nome': 'Martins Braga Dom',
        'Cpf': 87765432198,
        'Nascimento': '3/05/1998',
        'Cidade': 'Martenha - SP'
    },

    '12365432100': {
        'Nome': 'Brenda Martiz Faria',
        'Cpf': 12365432100,
        'Nascimento': '13/12/2001',
        'Cidade': 'Curitiba - PR'
    },

    '48165432100': {
        'Nome': 'Eduarda Gonzaga Enflads',
        'Cpf': 48165432100,
        'Nascimento': '27/07/1989',
        'Cidade': 'Porte Livre - PR'
    },
}

//console.log(dados['17999241788'].Nome)
const container = document.querySelector('.container')

for (dado in dados){
    card.innerHTML = ''

    var nome = dados[dado].Nome
    var cpf = dados[dado].Cpf
    var nascimento = dados[dado].Nascimento
    var cidade = dados[dado].Cidade

    const userDiv = document.createElement('div')
    userDiv.classList('card')
    userDiv.innerHTML = `
        <h3>${nome}</h3>
        <p><span class="label">Nascimento:</span> ${nascimento}</p>
        <p><span class="label">CPF:</span> ${cpf}</p>
        <p><span class="label">Onde mora:</span> ${cidade}</p>`

    container.appendChild(userDiv)
}

