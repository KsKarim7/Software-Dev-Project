const displayData = (data) => {
    document.getElementById("total-meals").innerText = data.length;

    const mealsContainer = document.getElementById("items-container");
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