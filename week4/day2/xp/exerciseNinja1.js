// 🌟 Exercise 1: Dog age to Human years
const data = [
  { name: 'Butters', age: 3, type: 'dog' },
  { name: 'Cuty', age: 5, type: 'rabbit' },
  { name: 'Lizzy', age: 6, type: 'dog' },
  { name: 'Red', age: 1, type: 'cat' },
  { name: 'Joey', age: 3, type: 'dog' },
  { name: 'Rex', age: 10, type: 'dog' },
];

// 1.a Using loop
let sumDogYears = 0;
for (let animal of data) {
  if (animal.type === 'dog') {
    sumDogYears += animal.age * 7;
  }
}
console.log("Exercise 1.a:", sumDogYears); // Output: 154

// 1.b Using reduce
const sumDogYearsReduce = data.reduce((sum, animal) => {
  return animal.type === 'dog' ? sum + animal.age * 7 : sum;
}, 0);
console.log("Exercise 1.b:", sumDogYearsReduce); // Output: 154

// 🌟 Exercise 2: Email cleanup
const userEmail3 = ' cannotfillemailformcorrectly@gmail.com ';
const cleanedEmail = userEmail3.trim();
console.log("Exercise 2:", cleanedEmail); // Output: "cannotfillemailformcorrectly@gmail.com"

// 🌟 Exercise 3: Employees #3
const users = [
  { firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
  { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
  { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
  { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
  { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
  { firstName: 'Wes', lastName: 'Reid', role: 'Instructor' },
  { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor' }
];

const userRoles = {};
users.forEach(({ firstName, lastName, role }) => {
  userRoles[`${firstName} ${lastName}`] = role;
});
console.log("Exercise 3:", userRoles);
/*
{
  'Bradley Bouley': 'Full Stack Resident',
  'Chloe Alnaji': 'Full Stack Resident',
  ...
}
*/

// 🌟 Exercise 4: Array to Object
const letters = ['x', 'y', 'z', 'z'];

// 4.a Using for loop
const countLettersLoop = {};
for (let char of letters) {
  countLettersLoop[char] = (countLettersLoop[char] || 0) + 1;
}
console.log("Exercise 4.a:", countLettersLoop); // { x:1, y:1, z:2 }

// 4.b Using reduce
const countLettersReduce = letters.reduce((acc, char) => {
  acc[char] = (acc[char] || 0) + 1;
  return acc;
}, {});
console.log("Exercise 4.b:", countLettersReduce); // { x:1, y:1, z:2 }
