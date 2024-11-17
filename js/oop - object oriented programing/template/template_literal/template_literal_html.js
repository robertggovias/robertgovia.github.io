import productData from './data.json' assert { type: 'json' };

document.addEventListener('DOMContentLoaded', () => {
  const productTemplate = document.getElementById('product-template');
  const productList = document.getElementById('product-list');

  // Function to render products dynamically
  const renderProducts = (products) => {
    products.forEach(product => {
      const templateContent = productTemplate.content.cloneNode(true);
      
      const imgElement = templateContent.querySelector('.product-image');
      const nameElement = templateContent.querySelector('.product-name');
      const descriptionElement = templateContent.querySelector('.product-description');
      const brandElement = templateContent.querySelector('.brand');
      const priceElement = templateContent.querySelector('.price');

      imgElement.src = product.Image;
      imgElement.alt = product.NameWithoutBrand;
      nameElement.textContent = product.Name;
      descriptionElement.innerHTML = product.DescriptionHtmlSimple;
      brandElement.textContent = product.Brand.Name;
      priceElement.textContent = `$${product.FinalPrice.toFixed(2)}`;

      productList.appendChild(templateContent);
    });
  };

  renderProducts(productData);
});