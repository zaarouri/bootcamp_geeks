let client = "John";

const groceries = {
  fruits: ["pear", "apple", "banana"],
  vegetables: ["tomatoes", "cucumber", "salad"],
  totalPrice: "20$",
  other: {
    paid: true,
    meansOfPayment: ["cash", "creditCard"]
  }
};

// 1. Display the fruits
const displayGroceries = () => {
  groceries.fruits.forEach(fruit => console.log(fruit));
};

// 2. Clone groceries and test behavior
const cloneGroceries = () => {
  let user = client; // primitive copy
  client = "Betty"; // only changes the original, not the copy
  console.log("user:", user); // => "John"

  let shopping = groceries; // reference copy
  shopping.totalPrice = "35$"; // modifies both shopping and groceries
  shopping.other.paid = false; // modifies both shopping.other and groceries.other

  console.log("groceries.totalPrice:", groceries.totalPrice); // => "35$"
  console.log("groceries.other.paid:", groceries.other.paid); // => false
};

// Run functions
displayGroceries();
cloneGroceries();
