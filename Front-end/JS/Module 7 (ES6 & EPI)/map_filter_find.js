// map 
const nums = [2, 3, 4];
const square = nums.map(x => x * x);

// filter
const prod = [
    { id: 1, name: 'samsung', price: 270, color: 'blue' },
    { id: 2, name: 'sony', price: 170, color: 'grey' },
    { id: 3, name: 'xiaomi', price: 150, color: 'grey' }
]

const filteredProduct = prod.filter((pd) => pd.color == 'grey');
// console.log(filteredProduct);

// find 
// if applies to multiple products then find gives you the first matched product
const foundProb = prod.find(pd => pd.id == 1);
console.log(foundProb);