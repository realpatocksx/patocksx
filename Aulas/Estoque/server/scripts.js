document.querySelector('.btn-add-product').addEventListener('click', () => {
    document.getElementById('formContainer').style.display = 'flex';
  });
  
  document.querySelector('.close-modal').addEventListener('click', () => {
    document.getElementById('productModal').style.display = 'none';
  });
  
  // Exemplo de funcionalidade básica de cadastro
  document.getElementById('productForm').addEventListener('submit', (e) => {
    e.preventDefault();
  
    const name = document.getElementById('name').value;
    const description = document.getElementById('description').value;
    const price = document.getElementById('price').value;
    const quantity = document.getElementById('quantity').value;
    const image = document.getElementById('image').value;
  
    const productGrid = document.getElementById('productGrid');
    const card = document.createElement('div');
    card.className = 'product-card';
    card.innerHTML = `
      <img src="${image}" alt="${name}">
      <div class="product-info">
        <h3>${name}</h3>
        <p>${description}</p>
        <strong>R$ ${price}</strong>
        <button class="btn-decrease">-</button>
        <button class="btn-increase">+</button>
      </div>
    `;
    productGrid.appendChild(card);
  
    document.getElementById('formContainer').style.display = 'none';
    e.target.reset();
  });