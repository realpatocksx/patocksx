const dados = {
    '17999241788': {
        'Nome': 'Pedro Henrique Castro',
        'Cpf': '179.992.417-88',
        'Nascimento': '25/02/2008',
        'Cidade': 'Vila Velha - ES'
    },
    '98765432100': {
        'Nome': 'João Victor Mendes da Silva',
        'Cpf': '987.654.321-00',
        'Nascimento': '17/09/1992',
        'Cidade': 'Perino - ES'
    },
    '68769932151': {
        'Nome': 'Maria Ferdinandes Aparecida',
        'Cpf': '687.699.321-51',
        'Nascimento': '29/11/1965',
        'Cidade': 'Avenida Braga - MG'
    },
    '87765432198': {
        'Nome': 'Martins Braga Dom',
        'Cpf': '877.654.321-98',
        'Nascimento': '03/05/1998',
        'Cidade': 'Martenha - SP'
    },
    '12365432100': {
        'Nome': 'Brenda Martiz Faria',
        'Cpf': '123.654.321-00',
        'Nascimento': '13/12/2001',
        'Cidade': 'Curitiba - PR'
    },
    '48165432100': {
        'Nome': 'Eduarda Gonzaga Enflads',
        'Cpf': '481.654.321-00',
        'Nascimento': '27/07/1989',
        'Cidade': 'Porte Livre - PR'
    }
};

// Seleciona o elemento que irá conter os cards
const container = document.querySelector('.container');

// Limpa o conteúdo existente dentro do container
container.innerHTML = '';

// Cria e insere cada card baseado nos dados
for (let dado in dados) {
    // Criação de cada card
    const userDiv = document.createElement('div');
    userDiv.classList.add('card');

    // Obtém as informações da pessoa
    const nome = dados[dado].Nome;
    const cpf = dados[dado].Cpf;
    const nascimento = dados[dado].Nascimento;
    const cidade = dados[dado].Cidade;

    // Define o conteúdo do card
    userDiv.innerHTML = `
        <h3>${nome}</h3>
        <p><span class="label">Nascimento:</span> ${nascimento}</p>
        <p><span class="label">CPF:</span> ${cpf}</p>
        <p><span class="label">Cidade:</span> ${cidade}</p>
    `;

    // Adiciona o card ao container
    container.appendChild(userDiv);
}