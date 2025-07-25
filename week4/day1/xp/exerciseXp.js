// 🌟 Exercise 1 : Scope

// #1
function funcOne() {
    let a = 5;
    if(a > 1) {
        a = 3;
    }
    alert(`inside the funcOne function ${a}`); // 3
}
funcOne()
// #1.2: Using const will throw an error because const can't be reassigned

// #2
let a = 0;
function funcTwo() {
    a = 5;
}
function funcThree() {
    alert(`inside the funcThree function ${a}`);
}
funcThree() // 0
funcTwo()
funcThree() // 5
// #2.2: Using const will throw an error when trying to reassign 'a'

// #3
function funcFour() {
    window.a = "hello";
}
function funcFive() {
    alert(`inside the funcFive function ${a}`);
}
funcFour()
funcFive() // "hello"

// #4
let a4 = 1;
function funcSix() {
    let a4 = "test";
    alert(`inside the funcSix function ${a4}`); // "test"
}
funcSix()
// #4.2: Using const here works since no reassignment happens

// #5
let a5 = 2;
if (true) {
    let a5 = 5;
    alert(`in the if block ${a5}`); // 5
}
alert(`outside of the if block ${a5}`); // 2
// #5.2: const behaves the same due to block scope


// 🌟 Exercise 2 : Ternary operator
const winBattle = () => true;
const experiencePoints = winBattle() ? 10 : 1;
console.log(experiencePoints); // 10


// 🌟 Exercise 3 : Is it a string ?
const isString = value => typeof value === 'string';
console.log(isString('hello')); // true
console.log(isString([1, 2, 4, 0])); // false


// 🌟 Exercise 4 : Find the sum
const sum = (a, b) => a + b;
console.log(sum(5, 7)); // 12


// 🌟 Exercise 5 : Kg and grams
function convertKgToGrams(weight) {
    return weight * 1000;
}
console.log(convertKgToGrams(2)); // 2000

const convert = function(weight) {
    return weight * 1000;
};
console.log(convert(3)); // 3000
// Function declaration is hoisted; expression is not.

const convertArrow = weight => weight * 1000;
console.log(convertArrow(4)); // 4000


// 🌟 Exercise 6 : Fortune teller
(function(children, partner, location, job) {
    const sentence = `You will be a ${job} in ${location}, and married to ${partner} with ${children} kids.`;
    document.body.innerHTML += `<p>${sentence}</p>`;
})(3, "Alice", "Tokyo", "Software Engineer");


// 🌟 Exercise 7 : Welcome
(function(username) {
    const navbar = document.getElementById("navbar");
    const div = document.createElement("div");
    div.innerHTML = `
        <span>Welcome, ${username}</span>
        <img src="https://i.pravatar.cc/40" alt="profile" style="border-radius: 50%;" />
    `;
    navbar.appendChild(div);
})("John");


// 🌟 Exercise 8 : Juice Bar
function makeJuice(size) {
    const ingredients = [];

    function addIngredients(ing1, ing2, ing3) {
        ingredients.push(ing1, ing2, ing3);
    }

    function displayJuice() {
        const sentence = `The client wants a ${size} juice, containing ${ingredients.join(', ')}.`;
        document.body.innerHTML += `<p>${sentence}</p>`;
    }

    addIngredients("orange", "mint", "lemon");
    addIngredients("pineapple", "ginger", "carrot");
    displayJuice();
}
makeJuice("medium");
