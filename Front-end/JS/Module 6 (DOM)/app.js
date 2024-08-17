// alert("Hilu")
// console.log("Hilu");
var head = document.getElementsByTagName("h1");
// console.log(head);
// console.log(document.getElementsByTagName("h1"));

var title = document.getElementById('title').style.backgroundColor = 'grey';

document.getElementById('title').style.removeProperty('backgroundColor');

// console.log(title);

var child = document.getElementsByClassName('child');
// console.log(child[0]);


var testDiv = document.getElementsByClassName("test");

// console.log(testDiv[0].childNodes[1].parentNode.parentNode.parentNode);

var newDiv = document.getElementById("newDiv");
function createEl() {
    var p = document.createElement("p");
    p.innerText = "New BD";
    newDiv.appendChild(p);
}


createEl();

document.getElementById("submit-btn").addEventListener("click", inputChange)

function inputChange(e) {
    // console.log("funk your browser");
    // createEl();
    var inputValue = document.getElementById("input").value;
    console.log(inputValue);
}