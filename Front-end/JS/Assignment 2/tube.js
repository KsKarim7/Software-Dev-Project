const loadNavData = () => {
    fetch("https://openapi.programming-hero.com/api/videos/categories")
        .then(res => res.json())
        .then(data => displayNav(data.data));
    // .then(data => console.log(data.data));
}



const displayNav = (data) => {
    // console.log(data);

    const dynamicNav = document.getElementById("dynamic-nav");
    data.forEach((option) => {
        const btn = document.createElement("span");

        btn.innerHTML = `<button onclick="loadItemsData('${option.category_id}'); toggleColor(this);" type="button" class="btn toggle me-2 mb-1" style="background-color: rgb(206, 205, 205); color: rgb(103, 103, 103);"><span class="fw-semibold">${option.category}</span></button>`


        dynamicNav.appendChild(btn);
    });
};

// Toggle color on navigation bar

const toggleColor = (button) => {
    const buttons = document.querySelectorAll('.toggle');

    //  resetting their colors
    buttons.forEach(btn => {
        btn.style.backgroundColor = 'rgb(206, 205, 205)';
        btn.style.color = 'rgb(103, 103, 103)';
    });

    // Changing the color of the clicked button
    button.style.backgroundColor = 'red';
    button.style.color = '#fff';
}



// Load and display items

const loadItemsData = async (id) => {
    try {
        const res = await fetch(`https://openapi.programming-hero.com/api/videos/category/${id}`);
        // const res = await fetch(`https://openapi.programming-hero.com/api/videos/category/1005`);
        const data = await res.json();
        displayItemsData(data.data);
        // console.log(data.data);
    }
    catch {
        err => {
            console.log(err);
        }
    }
}
// const loadItemsData = (id) => {
//     fetch(`https://openapi.programming-hero.com/api/videos/category/${id}`)
//         .then((res) => res.json())
//         .then((data) => displayItemsData(data.data));
//     // .then((data) => console.log(data.data));
// }



const displayItemsData = (data) => {
    const displayData = document.getElementById("items-container");
    data.forEach((item) => {
        const card = document.createElement("div");
        card.classList.add("grid-item");
        // <small>${item.others.posted_date ? convertTime(item.others.posted_date) : 0}</small>
        card.innerHTML = `
            
            <img src="${item.thumbnail}" style="width: 100%; height:60%; border-radius: 5%;" alt="">
            <div class="d-flex pt-3">
            <img class="" style="width: 8%; height:15%;   border-radius: 50%;" src="${item.authors[0].profile_picture}" alt="">
            <div class="ms-2 lh-1" style="color: rgb(147, 146, 146);">
            <p class="fw-bold text-dark">${item.title}</p>
            <p>${item.authors[0].profile_name} <span>${ifVerified(item.authors[0].verified)}</span></p>
            <p>${item.others.views}</p>
            </div>
            </div>
            `;
        displayData.appendChild(card);
        // document.getElementById("items-container").innerText = "";
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
function convertTime(sec) {
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;
    return `${hours}hrs ${minutes}min ${seconds} sec ago`;
}


// global default call
loadNavData();
loadItemsData(1001);