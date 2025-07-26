// 🚗 Car Inventory Data
const inventory = [
  { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
  { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
  { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
  { id: 4, car_make: "Land Rover", car_model: "Defender Ice Edition", car_year: 2010 },
  { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
];

// ✅ Part I: Find first Honda
const getCarHonda = (carInventory) => {
  const honda = carInventory.find(car => car.car_make === "Honda");
  return `This is a ${honda.car_make} ${honda.car_model} from ${honda.car_year}.`;
};

console.log("Part I Output:", getCarHonda(inventory));
// Output: This is a Honda Accord from 1983.

// ✅ Part II: Sort inventory by year (ascending)
const sortCarInventoryByYear = (carInventory) => {
  return [...carInventory].sort((a, b) => a.car_year - b.car_year);
};

console.log("Part II Output:", sortCarInventoryByYear(inventory));
