// Function that checks if all given values are truthy
function allTruthy(...args) {
  // Use .every() to test if every value is truthy using Boolean
  return args.every(Boolean);
}

// Test case 1: all values are true → should return true
console.log(allTruthy(true, true, true)); // ➞ true

// Test case 2: one false value → should return false
console.log(allTruthy(true, false, true)); // ➞ false

// Test case 3: includes 0 (which is falsy) → should return false
console.log(allTruthy(5, 4, 3, 2, 1, 0)); // ➞ false

// Test case 4: all truthy values (non-empty string, number, array) → true
console.log(allTruthy("hello", 123, [])); // ➞ true

// Test case 5: includes null (falsy) → should return false
console.log(allTruthy(null, "value", true)); // ➞ false
