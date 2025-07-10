// 🌟 Exercise 1 : List of people
const people = ["Greg", "Mary", "Devon", "James"];

// Part I
// 1. Remove “Greg”
people.shift();

// 2. Replace “James” with “Jason”
people[people.indexOf("James")] = "Jason";

// 3. Add your name to the end
people.push("Abdelmounime");

// 4. Log Mary’s index
console.log(people.indexOf("Mary"));

// 5. Copy of people without Mary and your name
const copy = people.slice(1, people.length - 1);
console.log(copy);

// 6. Index of “Foo”
console.log(people.indexOf("Foo")); // returns -1 because "Foo" is not in the array

// 7. Last element of the array
const last = people[people.length - 1];
console.log(last);

// Part II - Loops
// 1. Loop through array
for (let person of people) {
    console.log(person);
}

// 2. Loop and stop after “Devon”
for (let person of people) {
    console.log(person);
    if (person === "Devon") break;
}


// 🌟 Exercise 2 : Your favorite colors
const colors = ["blue", "red", "green", "black", "white"];

// Basic version
for (let i = 0; i < colors.length; i++) {
    console.log(`My #${i + 1} choice is ${colors[i]}`);
}

// Bonus version
const suffixes = ["st", "nd", "rd", "th", "th"];
for (let i = 0; i < colors.length; i++) {
    console.log(`My ${i + 1}${suffixes[i]} choice is ${colors[i]}`);
}


// 🌟 Exercise 3 : Repeat the question
let number = prompt("Enter a number:");
while (Number(number) < 10) {
    number = prompt("Enter a number again (must be 10 or more):");
}


// 🌟 Exercise 4 : Building Management
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
};

// 1. Number of floors
console.log(building.numberOfFloors);

// 2. Apartments on 1st and 3rd floors
console.log(building.numberOfAptByFloor.firstFloor + building.numberOfAptByFloor.thirdFloor);

// 3. Name of second tenant and rooms
const secondTenant = building.nameOfTenants[1];
console.log(secondTenant, building.numberOfRoomsAndRent[secondTenant.toLowerCase()][0]);

// 4. Rent check
const rentSarah = building.numberOfRoomsAndRent.sarah[1];
const rentDavid = building.numberOfRoomsAndRent.david[1];
const rentDan = building.numberOfRoomsAndRent.dan[1];

if (rentSarah + rentDavid > rentDan) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
}
console.log(building.numberOfRoomsAndRent.dan[1]);


// 🌟 Exercise 5 : Family
const family = {
    dad: "John",
    mom: "Jane",
    son: "Chris"
};

// Log keys
for (let key in family) {
    console.log(key);
}

// Log values
for (let key in family) {
    console.log(family[key]);
}


// Exercise 6 : Rudolf
const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'reindeer'
};

let sentence = "";
for (let key in details) {
    sentence += `${key} ${details[key]} `;
}
console.log(sentence.trim());


// Exercise 7 : Secret Group
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let society = names.map(name => name[0]).sort().join('');
console.log(society); // ABJKPS

