// Avaliação com estrelas
const stars = document.querySelectorAll('.star');
stars.forEach((star, index) => {
  star.addEventListener('click', () => {
    stars.forEach((s, i) => {
      s.classList.toggle('selected', i <= index);
    });
  });
});

// Mostrar/ocultar descrição completa
const btnMore = document.querySelector('.btn-more');
btnMore.addEventListener('click', () => {
  const hiddenText = document.querySelector('.hidden-text');
  if (hiddenText.style.display === 'none' || hiddenText.style.display === '') {
    hiddenText.style.display = 'inline';
    btnMore.textContent = 'Mostrar menos';
  } else {
    hiddenText.style.display = 'none';
    btnMore.textContent = 'Mostrar mais';
  }
});

// Seletores do carrossel
const imagesWrapper = document.querySelector('.images-wrapper');
const images = document.querySelector('.images');
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');

let currentIndex = 0; // Índice da imagem atual
const totalImages = images.children.length; // Número total de imagens

// Clonar as extremidades para o loop infinito
const firstImage = images.children[0].cloneNode(true); // Clona a primeira imagem
const lastImage = images.children[totalImages - 1].cloneNode(true); // Clona a última imagem
images.appendChild(firstImage); // Adiciona a primeira imagem ao final
images.insertBefore(lastImage, images.children[0]); // Adiciona a última imagem ao início

// Atualiza o carrossel
function updateCarousel() {
  const imageWidth = imagesWrapper.offsetWidth; // Largura do contêiner visível
  images.style.transform = `translateX(-${(currentIndex + 1) * imageWidth}px)`; // Ajusta posição com base no índice
}

// Navegação com loop infinito
prevBtn.addEventListener('click', () => {
  const imageWidth = imagesWrapper.offsetWidth;
  currentIndex--;
  images.style.transition = 'transform 0.5s ease-in-out';
  updateCarousel();
  
  // Quando chegar ao início, pula para o clone da última imagem
  if (currentIndex < 0) {
    setTimeout(() => {
      images.style.transition = 'none'; // Remove transição temporariamente
      currentIndex = totalImages - 1; // Ajusta índice
      updateCarousel();
    }, 500); // Sincroniza com o tempo da transição
  }
});

nextBtn.addEventListener('click', () => {
  const imageWidth = imagesWrapper.offsetWidth;
  currentIndex++;
  images.style.transition = 'transform 0.5s ease-in-out';
  updateCarousel();
  
  // Quando chegar ao final, pula para o clone da primeira imagem
  if (currentIndex >= totalImages) {
    setTimeout(() => {
      images.style.transition = 'none'; // Remove transição temporariamente
      currentIndex = 0; // Ajusta índice
      updateCarousel();
    }, 500); // Sincroniza com o tempo da transição
  }
});

// Ajuste para redimensionamento da janela
window.addEventListener('resize', updateCarousel);

// Configuração inicial ao carregar a página
window.addEventListener('load', () => {
  const imageWidth = imagesWrapper.offsetWidth;
  images.style.transition = 'none'; // Sem animação no início
  images.style.transform = `translateX(-${imageWidth}px)`; // Começa no clone correto
});