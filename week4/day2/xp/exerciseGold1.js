// 🌟 Exercise 1: Analyzing map
const result1 = [1, 2, 3].map(num => {
  if (typeof num === 'number') return num * 2;
  return; // implicitly returns undefined if not a number
});
console.log("Exercise 1 Output:", result1); // [2, 4, 6]

// 🌟 Exercise 2: Analyzing reduce
const result2 = [[0, 1], [2, 3]].reduce(
  (acc, cur) => acc.concat(cur),
  [1, 2]
);
console.log("Exercise 2 Output:", result2); // [1, 2, 0, 1, 2, 3]

// 🌟 Exercise 3: Analyze map index
const arrayNum = [1, 2, 4, 5, 8, 9];
const newArray = arrayNum.map((num, i) => {
  console.log("num:", num, "index:", i);
  // alert(num); // Uncomment in browser to see popups
  return num * 2;
});
// i is the index of each element => 0 to 5

// 🌟 Exercise 4.1: Nested arrays flattening
const array = [[1], [2], [3], [[[4]]], [[[5]]]];
const flatArray = array.flat(2);
console.log("Exercise 4.1 Output:", flatArray); // [1, 2, 3, [4], [5]]

// 🌟 Exercise 4.2: Join greeting arrays into sentences
const greeting = [["Hello", "young", "grasshopper!"], ["you", "are"], ["learning", "fast!"]];
const greetingSentences = greeting.map(sentence => sentence.join(" "));
console.log("Exercise 4.2 Output:", greetingSentences); // ["Hello young grasshopper!", "you are", "learning fast!"]

// 🌟 Exercise 4.3: Turn into one string
const greetingFlatString = greeting.flat().join(" ");
console.log("Exercise 4.3 Output:", greetingFlatString); // 'Hello young grasshopper! you are learning fast!'

// 🌟 Exercise 4.4: Free the trapped number
const trapped = [[[[[[[[[[[[[[[[[[[[[[[[[[3]]]]]]]]]]]]]]]]]]]]]]]]]];
const freed = trapped.flat(Infinity);
console.log("Exercise 4.4 Output:", freed); // [3]
