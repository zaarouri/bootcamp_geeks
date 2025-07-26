// 🌟 Exercise 1 : Menu
const menu = [
  { type: "starter", name: "Houmous with Pita" },
  { type: "starter", name: "Vegetable Soup with Houmous peas" },
  { type: "dessert", name: "Chocolate Cake" }
];

// 1.1: Check if at least one dessert
const hasDessert = menu.some(item => item.type === "dessert");
console.log("Has dessert?", hasDessert ? "Yes" : "No");

// 1.2: Check if all items are starters
const allStarters = menu.every(item => item.type === "starter");
console.log("All starters?", allStarters);

// 1.3: Check for main course, if none, add one
const hasMain = menu.some(item => item.type === "main");
if (!hasMain) {
  menu.push({ type: "main", name: "Grilled Chicken with Potatoes" });
}
console.log("Menu after checking main:", menu);

// 1.4: Add 'vegetarian' key based on ingredients
const vegetarian = ["vegetable", "houmous", "eggs", "vanilla", "potatoes"];
menu.forEach(item => {
  const lowerName = item.name.toLowerCase();
  item.vegetarian = vegetarian.some(veg => lowerName.includes(veg));
});
console.log("Menu with vegetarian flag:", menu);


// 🌟 Exercise 2 : Chop into chunks
const string_chop = (str, size) => {
  const result = [];
  for (let i = 0; i < str.length; i += size) {
    result.push(str.slice(i, i + size));
  }
  return result;
};
console.log("Chop result:", string_chop('developers', 2)); // ["de", "ve", "lo", "pe", "rs"]


// 🌟 Exercise 3 : Search word
const search_word = (sentence, word) => {
  const count = sentence.split(" ").filter(w => w === word).length;
  return `'${word}' was found ${count} ${count === 1 ? "time" : "times"}.`;
};
console.log(search_word('The quick brown fox', 'fox')); // 'fox' was found 1 times.


// 🌟 Exercise 4 : Reverse array (in-place)
const reverseArray = arr => {
  for (let i = 0; i < Math.floor(arr.length / 2); i++) {
    let temp = arr[i];
    arr[i] = arr[arr.length - 1 - i];
    arr[arr.length - 1 - i] = temp;
  }
  return arr;
};
console.log("Reverse [1,2,3,4,5]:", reverseArray([1,2,3,4,5]));         // [5,4,3,2,1]
console.log("Reverse [1,2]:", reverseArray([1,2]));                     // [2,1]
console.log("Reverse []:", reverseArray([]));                          // []
console.log("Reverse long:", reverseArray([1,2,3,4,5,6,7,8,9,10]));     // [10...1]
