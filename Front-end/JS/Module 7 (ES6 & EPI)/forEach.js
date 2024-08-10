const prods = [
    { id: 1, name: 'samsung', price: 270, color: 'blue' },
    { id: 2, name: 'sony', price: 170, color: 'grey' },
    { id: 3, name: 'xiaomi', price: 150, color: 'grey' }
]

const productContainer = document.getElementById("product-container");
const res = prods.forEach((prod) => {
    // console.log(prod);
    const h1 = document.createElement('h1');
    h1.innerText = prod.name;
    productContainer.appendChild(h1);
})