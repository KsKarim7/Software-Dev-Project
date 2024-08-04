// alert("Hilu")
console.log("Hilu");
var head = document.getElementsByTagName("h1");
console.log(head);
// console.log(document.getElementsByTagName("h1"));

var title = document.getElementById('title').style.backgroundColor = 'grey';

document.getElementById('title').style.removeProperty('backgroundColor');

console.log(title);

var child = document.getElementsByClassName('child');
console.log(child[0]);