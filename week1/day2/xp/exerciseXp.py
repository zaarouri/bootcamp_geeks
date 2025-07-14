# Erercise 1 

print("-"*30)
print("Exercise 1 : Dictionary")
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict = {}
dict = zip(keys, values)
print (list(dict))
# Exercise 2
print("")
print("Exercise 2 : Family")
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0
for key , value in family.items() :
    if value < 3 :
        continue
    elif value >3 and value <12 :
        total_cost += 10
    elif value >12 :
        total_cost+=15
print(total_cost)

#Exercise 3
print("-"*30)
print("Exercise 3 : Zara")
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2

print("Zara serves:", ", ".join(brand["type_of_clothes"]))

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
    
brand.pop("creation_date", None)
print("Last international competitor:", brand["international_competitors"][-1])
print("Major colors in the US:", ", ".join(brand["major_color"]["US"]))
print("Number of keys in brand dictionary:", len(brand))
print("Keys in brand dictionary:", list(brand.keys()))


# Exercise 4
print("-"*30)
print("Exercise 4 : City")
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

describe_city("Paris", "France")
describe_city("Tokyo")
# Exercise 5 
print("-"*30)
print("Exercise 5 : Guess the number")
import random 
rand = random.randint(1, 100)
while 1 :
    input_number = int(input("enter a number between 1 and 100"))
    if input_number != rand :
        print(f"fail Fail! Your number: {input_number}, Random number: {rand}")
    else :
        print("Success!")
        break
   
# Exercise 6
print("-"*30)
print("Exercise 6 : T-Shirt")
def make_shirt(size="large",text = "prada"):
    print(f"Shir{text} of size {size} is made")
make_shirt()
make_shirt(size="medium")
make_shirt("small", "zara")

make_shirt(size="extra large", text="h&m")
make_shirt(text="unknown", size="small")
# Exercise 7
print("-"*30)
print("Exercise 7 : Temperature")
def get_random_temp() :
    rnd = random.randint(1, 4)
    if rnd ==1 :
        return round(random.uniform(-10, 10), 1)
    elif rnd ==2 :
        return round(random.uniform(10, 20), 1)
    elif rnd ==3 :
        return round(random.uniform(20, 30), 1)
    elif rnd ==4 :
        return round(random.uniform(30, 40), 1)
def main() :
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0 :
        print(f"Brrr, that’s freezing! Wear some extra layers today.")
    elif temp >0 and temp < 16 :
        print(f"Quite chilly! Don’t forget your coat.")
    elif temp >16 and temp < 23 :
        print(f"Nice weather.")
    elif temp >24 and temp < 32 :
        print(f"A bit warm, stay hydrated")
    elif temp > 32 and temp < 40 :
        print(f"It’s really hot! Stay cool.")
main()
# Exercise 8 
print("-"*30)
print("Exercise 8 : Pizza Topping")

pizza_toppings = []
total_cost = 10  # base price

while True:
    pizza_topping = input("Enter a pizza topping (type 'quit' to exit): ").lower()

    if pizza_topping == "quit":
        break

    print(f"Adding {pizza_topping} to your pizza.")
    pizza_toppings.append(pizza_topping)
    total_cost += 2.50
    print(f"The total cost of your pizza is ${total_cost:.2f}")
    print("your pizza has the following toppings:", ", ".join(pizza_toppings))