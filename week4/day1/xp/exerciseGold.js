// Exercise 1
const landscape = () => {
  let result = "";
  const flat = x => { for (let i = 0; i < x; i++) result += "_"; };
  const mountain = x => {
    result += "/";
    for (let i = 0; i < x; i++) result += "'";
    result += "\\";
  };
  flat(4);
  mountain(4);
  flat(4);
  return result;
};
console.log("Exercise 1 Output:", landscape());

// Exercise 2
const addTo = x => y => x + y;
const addToTen = addTo(10);
console.log("Exercise 2 Output:", addToTen(3));

// Exercise 3
const curriedSum1 = a => b => a + b;
console.log("Exercise 3 Output:", curriedSum1(30)(1));

// Exercise 4
const curriedSum2 = a => b => a + b;
const add5 = curriedSum2(5);
console.log("Exercise 4 Output:", add5(12));

// Exercise 5
const compose = (f, g) => a => f(g(a));
const add1 = x => x + 1;
const add5Compose = x => x + 5;
console.log("Exercise 5 Output:", compose(add1, add5Compose)(10));
