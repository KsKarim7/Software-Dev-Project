const loadData = () => {
    fetch("https://jsonplaceholder.typicode.com/comments")
        .then((res) => res.json())
        .then((data) => displayData(data));
}

// loadData();

const displayData = (data) => {
    document.getElementById("total-data").innerText = data.length;
}