// 🌟 Exercise 1 : Promise.all()

// Three promises
const promise1 = Promise.resolve(3);
const promise2 = 42; // Not a Promise, but will be automatically wrapped
const promise3 = new Promise((resolve, reject) => {
  setTimeout(resolve, 3000, 'foo'); // resolves after 3s with 'foo'
});

// Using Promise.all
Promise.all([promise1, promise2, promise3])
  .then(values => {
    console.log("Exercise 1 - Promise.all resolved:", values);
  })
  .catch(error => {
    console.log("Exercise 1 - One of the promises failed:", error);
  });




// 🌟 Exercise 2 : Analyse Promise.all()

function timesTwoAsync(x) {
  return new Promise(resolve => resolve(x * 2));
}

const arr = [1, 2, 3];

// map each element to a Promise that doubles it
const promiseArr = arr.map(timesTwoAsync);

// Wait for all to resolve
Promise.all(promiseArr)
  .then(result => {
    console.log("Exercise 2 - Promise.all result:", result);
  });


