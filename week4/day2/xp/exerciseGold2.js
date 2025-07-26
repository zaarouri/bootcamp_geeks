// 🌟 Exercise 1: Sum elements
const sumArray = arr => arr.reduce((sum, num) => sum + num, 0);
console.log("Exercise 1:", sumArray([1, 2, 3, 4])); // 10

// 🌟 Exercise 2: Remove duplicates
const removeDuplicates = arr => [...new Set(arr)];
console.log("Exercise 2:", removeDuplicates([1, 2, 2, 3, 4, 4, 5])); // [1, 2, 3, 4, 5]

// 🌟 Exercise 3: Remove certain values
const cleanArray = arr => arr.filter(
  item => item !== false && item !== null && item !== 0 && item !== "" && item !== undefined && !Number.isNaN(item)
);
console.log("Exercise 3:", cleanArray([NaN, 0, 15, false, -22, '', undefined, 47, null])); // [15, -22, 47]

// 🌟 Exercise 4: Repeat please!
const repeat = (str, n = 1) => str.repeat(n);
console.log("Exercise 4:", repeat("Ha!", 3)); // "Ha!Ha!Ha!"

// 🌟 Exercise 5: Turtle & Rabbit
const startLine = '     ||<- Start line';
let turtle = '🐢';
let rabbit = '🐇';

// Align both animals under the start
turtle = turtle.padStart(9);
rabbit = rabbit.padStart(9);

console.log("Exercise 5:");
console.log(startLine);
console.log(turtle);
console.log(rabbit);

// Bonus: Explanation
const styledTurtle = turtle.trim().padEnd(9, '=');
console.log("Styled Turtle:", styledTurtle);
// Explanation:
// - `trim()` removes spaces => '🐢'
// - `padEnd(9, '=')` => '🐢======='
