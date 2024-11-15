// Seleciona o menu toggle e os links de navegação
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

// Adiciona um evento de clique ao menu toggle
menuToggle.addEventListener('click', () => {
    // Adiciona ou remove a classe 'active' para abrir ou fechar o menu
    menuToggle.classList.toggle('active');
    navLinks.classList.toggle('active');
});





