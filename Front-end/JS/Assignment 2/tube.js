const loadData = () => {
    fetch("https://openapi.programming-hero.com/api/videos/categories")
        .then(res => res.json())
        .then(data => displayData(data.data));
}

loadData();


const displayData = (data) => {
    // console.log(data);

    const dynamicNav = document.getElementById("dynamic-nav");
    data.forEach((option) => {
        const btn = document.createElement("span");

        btn.innerHTML = `<button type="button" class="btn me-2 mb-1" style="background-color: rgb(206, 205, 205); color: rgb(103, 103, 103);"><span class="fw-semibold">${option.category}</span></button>`


        dynamicNav.appendChild(btn);
    });
};