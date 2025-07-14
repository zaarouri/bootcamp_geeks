const numbers = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8];

console.log(numbers.toString());      
console.log(numbers.join());          
console.log(numbers.join("+"));      
console.log(numbers.join(" "));        
console.log(numbers.join(""));         


for (let i = 0; i < numbers.length; i++) {
    for(let j = i + 1; j < numbers.length; j++) {
        if (numbers[i] > numbers[j]) {
            let temp = numbers[i];
            numbers[i] = numbers[j];
            numbers[j] = temp;
            console.log(numbers.join(" "));
            
        }
    }
}
