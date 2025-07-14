// Exercise 1 : Checking the BMI
// Create person objects
const person1 = {
  fullName: "John Smith",
  mass: 80, // kg
  height: 1.8, // meters
  calcBMI: function() {
    this.bmi = this.mass / (this.height ** 2);
    return this.bmi;
  }
};

const person2 = {
  fullName: "Jane Doe",
  mass: 70,
  height: 1.65,
  calcBMI: function() {
    this.bmi = this.mass / (this.height ** 2);
    return this.bmi;
  }
};

// Function to compare BMIs
function compareBMI(p1, p2) {
  const bmi1 = p1.calcBMI();
  const bmi2 = p2.calcBMI();

  if (bmi1 > bmi2) {
    console.log(`${p1.fullName} has the higher BMI: ${bmi1.toFixed(2)}`);
  } else if (bmi2 > bmi1) {
    console.log(`${p2.fullName} has the higher BMI: ${bmi2.toFixed(2)}`);
  } else {
    console.log(`Both have the same BMI: ${bmi1.toFixed(2)}`);
  }
}

// Call the function
compareBMI(person1, person2);
// exercise 2 
