// after calling the desired api, it will return a promise, either it will resolve or success

// fetch("https://fakestoreapi.com/products/1")
//     .then(res => res.json())
//     .then(data => {
//         console.log(data);
//     })
//     .catch((err) => {
//         console.log(err);
//     })


// const getData = new Promise(function (resolve, reject) {
//     return reject("no data found");
// });

// getData.then(data => console.log(data)).catch((err)=>console.log(err));


// fetch("https://fakestoreapi.com/products/1")
//     .then(res => res.json())
//     .then(data => console.log(data))
//     .catch(err => console.log(err));


const loadData = async () => {
    try {
        const res = await fetch("https://fakestoreapi.com/products/1");
        // console.log(res.json);
        const data = await res.json();
        console.log(data);
    } catch {
        (err) => {
            console.log(err);
        };
    }
};

loadData();

