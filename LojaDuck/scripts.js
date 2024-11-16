// Seleciona o menu toggle e os links de navegação
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

// Adiciona um evento de clique ao menu toggle
menuToggle.addEventListener('click', () => {
    // Adiciona ou remove a classe 'active' para abrir ou fechar o menu
    menuToggle.classList.toggle('active');
    navLinks.classList.toggle('active');
});

//Butao Da Categoria
const clickcategory = document.querySelector('.category-button')

clickcategory.addEventListener('click', () => {
    clickcategory.innerHTML = `
        <select id="select">
            <option value='0'>Destaques</option>
            <option value="1">Acessorios De Casa</option>
            <option value="2">Acessorios De Tech</option>
            <option value="3">Moda Masculina e Feminina</option>
        </select>
    `
})