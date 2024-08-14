const loadNavData = () => {
    fetch("https://openapi.programming-hero.com/api/videos/categories")
        .then(res => res.json())
        .then(data => displayNav(data.data));
}

loadNavData();


const displayNav = (data) => {
    // console.log(data);

    const dynamicNav = document.getElementById("dynamic-nav");
    data.forEach((option) => {
        const btn = document.createElement("span");

        btn.innerHTML = `<button type="button" class="btn me-2 mb-1" style="background-color: rgb(206, 205, 205); color: rgb(103, 103, 103);"><span class="fw-semibold">${option.category}</span></button>`


        dynamicNav.appendChild(btn);
    });
};


// Load and display items

const loadItemsData = () => {
    fetch("https://openapi.programming-hero.com/api/videos/category/1000")
        .then((res) => res.json())
        .then((data) => displayItemsData(data.data));
    // .then((data) => console.log(data.data));
}

loadItemsData();


const displayItemsData = (data) => {
    const displayData = document.getElementById("items-container");
    data.forEach((item) => {
        const card = document.createElement("div");
        card.classList.add("grid-item");
        card.innerHTML = `
        <img src="${item.thumbnail}" style="width: 100%; height:60%; border-radius: 5%;" alt="">
        <div class="d-flex py-3">
            <img class="" style="width: 8%; height:15%;   border-radius: 50%;" src="${item.authors[0].profile_picture}" alt="">
            <div class="ms-2 lh-1" style="color: rgb(147, 146, 146);">
                <p class="fw-bold text-dark">${item.title}</p>
                <p>${item.authors[0].profile_name} <span>${ifVerified(item.authors[0].verified)}</span></p>
                <p>${item.others.views}</p>
            </div>
        </div>
        `;
        displayData.appendChild(card);
    })
}

function ifVerified(verified) {
    if (verified) {
        return '<i class="fa fa-check-circle ms-2" style="color: #3471da;"></i>';
    }
    else {
        return '';
    }
}


