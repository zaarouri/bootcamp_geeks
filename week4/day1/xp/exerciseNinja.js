const mergeWords = str => next => 
  next === undefined ? str : mergeWords(`${str} ${next}`);



console.log(mergeWords('There')('is')('no')('spoon.')()); // 'There is no spoon.'
console.log(mergeWords('Hello')());                       // 'Hello'
