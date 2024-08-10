// const num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
// console.log(Math.max(...num));
// console.log(typeof num);


// Arrow Function


// code in one line will be implicitly returned by the arrow function
const func = () => 2 * 2;
console.log(func());


const funcc = () => {
    console.log("Hello");
    return "Boss";
}

// Array destructuring

const arr = [1, 2, 3, 4, 5];
const [a, b, ...rest] = arr;
console.log(a, b, rest);


// object destructuring

const obj = {
    name: "John",
    age: 30,
    job: "Developer",
    address: {
        street: "123 Main St",
        city: "New York",
        state: "NY"
    },
    linkedin: "open to work"
};

const { name, age, job, address: { street }, linkedin } = obj;
console.log(street, job, address);