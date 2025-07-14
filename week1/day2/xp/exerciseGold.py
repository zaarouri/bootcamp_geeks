# Exercise 1 & 2
print("-"*30)
print("Exercise 1 : birthday")
birthdays = {
    "abdelmounime": "2001-06-07",
    "shihab": "2000-06-07",
    "salma": "2000-04-25",
    "marouan": "2003-06-11",
    "yassmine": "2001-07-07"
}
print("Welcome! You can look up the birthdays of the following people:")
print(", ".join(birthdays.keys()))
name = input("Enter a name to look up their birthday: ")

if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}")
else:
    print(f"Sorry, we don’t have the birthday information for {name}")
    birthdays[name] = input("What is their birthday? (YYYY-MM-DD) ")
    print(f"Thank you! We have added {name}'s birthday to our database.")


print("-"*30)
print("Exercise 4 : Double Dice")

import random

def throw_dice():
    return random.randint(1, 6)

def throw_until_doubles():
    throws = 0
    while True:
        die1 = throw_dice()
        die2 = throw_dice()
        throws += 1
        if die1 == die2:
            break
    return throws

def main():
    all_throws = []
    for _ in range(100):
        result = throw_until_doubles()
        all_throws.append(result)

    total = sum(all_throws)
    average = total / len(all_throws)

    print(f"Total throws to get 100 doubles: {total}")
    print(f"Average throws to reach doubles: {round(average, 2)}")

main()