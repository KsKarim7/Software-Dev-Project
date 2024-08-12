const loadData = (global) => {
    const searchText = document.getElementById("search-field").value;
    // console.log(searchText)
    fetch(`https://www.themealdb.com/api/json/v1/1/search.php?f=${searchText ? searchText : global}`)
        .then((res) => res.json())
        .then((data) => displayData(data.meals));
};


const displayData = (data) => {
    document.getElementById("total-meals").innerText = data.length;

    const mealsContainer = document.getElementById("meals-container");
    data.forEach((meal) => {
        const card = document.createElement("div");
        card.classList.add("box");
        card.innerHTML = `
        <img class="box-img" src="${meal.strMealThumb}" alt="">
        <h2>${meal?.strMeal}</h2>
        <p>${meal.strInstructions.slice(0, 100)}</p>
        <button 
        onclick="displayModal('${meal.idMeal}')" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
        Details
        </button>
        `;
        mealsContainer.appendChild(card);
    });
};


const displayModal = async (id) => {

    try {
        const res = await fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${id}`);
        const data = await res.json();
        console.log(data);
    }
    catch {
        err => {
            console.log(err);
        }
    }
}

// global default call
loadData("a");