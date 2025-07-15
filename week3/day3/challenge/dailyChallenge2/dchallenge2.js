// Prompt the user
let input = "Hello, World, in, a, frame";

// Split into array and trim whitespace
let words = input.split(',').map(word => word.trim());

// Find longest word length
let maxLength = Math.max(...words.map(word => word.length));

// Build the top/bottom border
let border = '*'.repeat(maxLength + 4);

// Print the framed output
console.log(border);
for (let word of words) {
  let padding = ' '.repeat(maxLength - word.length);
  console.log(`* ${word}${padding} *`);
}
console.log(border);

