/*const titulo = document.querySelector('#titulo')
const categoria = document.querySelector('#categoria')
const descricao = document.querySelector('#descricao')*/

noticias = {
    'Crime': {
        'Titulo': 'Jovem Rouba Traficando',
        'Categoria': 'Crime',
        'Descricao': 'Jovem rouba droga de traficando e faz lavagem de dinheiro'
    },

    'Cibeseguranca': {
        'Titulo': 'Hacker Anonimo',
        'Categoria': 'Cibeseguranca',
        'Descricao': 'hackear anonimo supostamente faz lavagem de dinheiro por bitcoin'
    },

    'Banco_Central': {
        'Titulo': 'Jovem Ganha na MegaCena',
        'Categoria': 'Banco Central',
        'Descricao': 'Jovem ganha 1real na MegaCena e ficar revoltado'
    },
}

const container = document.querySelector('#container')
container.innerHTML = ''

for (let item in noticias){

    const createDiv = document.createElement('section')
    createDiv.classList.add('card')

    const titulo = noticias[item].Titulo
    const descricao = noticias[item].Descricao
    const categoria = noticias[item].Categoria

    createDiv.innerHTML = `
        <h1> ${titulo} </h1>
        <p> ${categoria} </p>
        <p> ${descricao} </p>
        <input class="botao" type="submit" value="Acessar">`

    container.appendChild(createDiv)
}

const botao = document.querySelector('.botao')
addEventListener('click', click => {
    alert('Ainda Em Desenvolvimento')
})