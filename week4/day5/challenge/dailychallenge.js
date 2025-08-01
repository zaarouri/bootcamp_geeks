function isAnagram(a, b) {
  const normalize = (s) =>
    s
      .toLowerCase()
      .replace(/\s+/g, '')
      .split('')
      .sort()
      .join('');

  return normalize(a) === normalize(b);
}

// Examples
console.log(isAnagram('Astronomer', 'Moon starer'));    
console.log(isAnagram('School master', 'The classroom')); 
console.log(isAnagram('The Morse Code', 'Here come dots'));
console.log(isAnagram('hello', 'world'));           
