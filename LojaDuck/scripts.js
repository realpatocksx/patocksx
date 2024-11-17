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
const clickcategory = document.querySelector('.category-button');
const dropdownMenu = document.querySelector('.dropdown-menu');

clickcategory.addEventListener('click', () => {
    // Alterna a visibilidade do menu ao clicar no botão
    dropdownMenu.style.display = dropdownMenu.style.display === 'none' ? 'block' : 'none';
});

// Fecha o menu dropdown ao clicar fora dele
document.addEventListener('click', (event) => {
    if (!clickcategory.contains(event.target) && !dropdownMenu.contains(event.target)) {
        dropdownMenu.style.display = 'none';
    }
});


