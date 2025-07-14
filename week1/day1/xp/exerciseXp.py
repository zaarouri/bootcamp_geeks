#Exercise 1 : Hello World
for i in range(0,4):
    print("hello word")
#Exercise 2 : Some Math
result =(99^3)*8
print(f"the result of 99 to the power of 3, times 8 is {result} ")
#Exercise 3 : What’s your name ?
names= {
    "abdelmounime": "hiking",
    "shihab": "stalking",
    "salma": "eating healty",
    "marouan": "trading",
    "yassmine": "beauty makeup"
}
user_name = input("What's your name? ").strip().lower()
if user_name in names:
    interest = names[user_name]
    print(f"Hey {user_name.title()}! I heard you like {interest}. That's awesome! ")
else:
    print(f"{user_name.title()}? Hmm... you're not in our secret interest club yet!  Want to join Geeks?")
    user_interest = input("Tell me, what's something you really enjoy doing? ").strip().lower()
    names[user_name] = user_interest
    print(f"Nice! Welcome to Geeks, {user_name.title()} — lover of {user_interest}! 😎")
    
    
# Exercise 4 : Tall enough to ride a roller coaster
user_input = int(input("Please enter your height in cm : "))
if user_input < 145 :
    print("sorry ,you are not allowed to ride ")
else :
    print("are tall enough to ride ")
#Exercise 5 : Favorite Numbers
my_fav_numbers = {3, 7}
print("My favorite numbers:", my_fav_numbers)
my_fav_numbers.add(1)
my_fav_numbers.add(9)
print("After adding two numbers:", my_fav_numbers)
my_fav_numbers.remove(9)
print("After removing the last added number:", my_fav_numbers)
friend_fav_numbers = {4, 7, 10}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print("Our favorite numbers:", our_fav_numbers)
#Exercise 6: Tuple
my_tuple = (1, 2, 3)

try:
    my_tuple.append(4)  
except AttributeError as e:
    print("Error:", e)

new_tuple = my_tuple + (4, 5)
print("Original tuple:", my_tuple)
print("New tuple:", new_tuple)
#Exercise 7: List Manipulation

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apples_count = basket.count("Apples")
print("Apples appear", apples_count, "time(s) in the list.")
basket.clear()
print("Final basket:", basket)
# Exercise 8 : Sandwich Orders
sandwich_orders = [
    "Tuna sandwich", "Pastrami sandwich", "Avocado sandwich",
    "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"
]

print("The deli has run out of pastrami.\n")

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(-1)
    print(f"I made your {current_sandwich.lower()}")
    finished_sandwiches.append(current_sandwich)


for sandwich in finished_sandwiches:
    print(f"i made your - {sandwich}")
