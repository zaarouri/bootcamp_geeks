// 🌟 Exercise 1 : Comparison
function compareToTen(num) {
  return new Promise((resolve, reject) => {
    if (num <= 10) {
      resolve(`${num} is less than or equal to 10`);
    } else {
      reject(`${num} is greater than 10`);
    }
  });
}

// Test cases for Exercise 1
compareToTen(15)
  .then(result => console.log("Exercise 1:", result))
  .catch(error => console.log("Exercise 1:", error));

compareToTen(8)
  .then(result => console.log("Exercise 1:", result))
  .catch(error => console.log("Exercise 1:", error));


// 🌟 Exercise 2 : Promises
const delayedSuccess = new Promise((resolve) => {
  setTimeout(() => {
    resolve("success");
  }, 4000); // Resolves after 4 seconds
});

// Test case for Exercise 2
delayedSuccess.then(result => console.log("Exercise 2:", result));


// 🌟 Exercise 3 : Resolve & Reject

// Resolves with value 3
const resolvedPromise = Promise.resolve(3);
resolvedPromise.then(val => console.log("Exercise 3 - Resolved:", val));

// Rejects with error "Boo!"
const rejectedPromise = Promise.reject("Boo!");
rejectedPromise.catch(err => console.log("Exercise 3 - Rejected:", err));



