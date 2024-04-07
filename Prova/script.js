const menu = document.querySelector('.menu');
const navLinks = document.querySelector('.links');

menu.addEventListener('click', () => {
	navLinks.classList.toggle('open');
});

navLinks.addEventListener('click', () => {
	navLinks.classList.remove('open');
});
