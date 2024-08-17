console.log("My name is Khan");

var num1 = "12.2321212"
console.log(parseFloat(num1).toFixed(3));


var weather = 'gloomy';

if (weather == 'rainy') {
    console.log("Let us go for a date baby!");
}
else if (weather == 'sunny') {
    console.log("Ughhh!");
}
else {
    console.log("Just procrastinate!");
}

var robot = {
    name: "RoboCop",
    age: 30,
    speak: function () {
        console.log("Beep beep!");
    }
}

// console.log(Object.keys(robot))
// console.log(Object.values(robot))
// console.log(Object.entries(robot))
// console.log(robot.speak());

var friends = ["a", "b", "c", "d", "e"];
friends.push("z");
friends.pop("z");
friends.unshift("e");
friends.shift();
console.log(friends);
console.log(['a', 'b'].concat('c'));
console.log(friends.slice(2, 4));


for (var i = 0; i < friends.length; i++) {
    console.log(friends[i]);
}