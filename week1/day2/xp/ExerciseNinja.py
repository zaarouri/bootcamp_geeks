# Exercise 1
print("-"*30)
print("Exercise 1 : Cars")

car_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
car_list = car_string.split(", ")

print(f"There are {len(car_list)} manufacturers in the list.")


print("Manufacturers in reverse (Z-A):", sorted(car_list, reverse=True))


count_with_o = len([c for c in car_list if 'o' in c.lower()])
count_without_i = len([c for c in car_list if 'i' not in c.lower()])

print(f"Manufacturers with the letter 'o': {count_with_o}")
print(f"Manufacturers without the letter 'i': {count_without_i}")


car_list_dup = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
unique_cars = list(set(car_list_dup))
print(f"Unique manufacturers: {', '.join(unique_cars)}")
print(f"Now there are {len(unique_cars)} companies in the list.")


reversed_sorted = [name[::-1] for name in sorted(unique_cars)]
print("Manufacturers (A-Z) with names reversed:", reversed_sorted)

# Exercise 2
print("-"*30)
print("Exercise 2 : What’s your name?")

def get_full_name(first_name, last_name, middle_name=None):
    if middle_name:
        return f"{first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}"
    else:
        return f"{first_name.capitalize()} {last_name.capitalize()}"

print(get_full_name("john", "lee", "hooker"))
print(get_full_name("bruce", "lee"))

# Exercise 3
print("-"*30)
print("Exercise 3 : From English to Morse")

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

def english_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(c.upper(), '') for c in text)

def morse_to_english(morse):
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    return ''.join(reverse_dict.get(c, '') for c in morse.split(' '))

# Examples:
print(english_to_morse("hello world"))
print(morse_to_english(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."))

# Exercise 2
print("-"*30)
print("Exercise 2 : Birthday Lookup")

birthdays = {
    "Alice": "1990/04/12",
    "Bob": "1985/07/30",
    "Charlie": "1992/12/01",
    "Diana": "1999/09/20",
    "Eve": "2001/01/15"
}

print("Welcome! You can look up the birthdays of the following people:")
print(", ".join(birthdays.keys()))
name = input("Enter a name to look up their birthday: ")

if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}")
else:
    print(f"Sorry, we don’t have the birthday information for {name}")

# Exercise 3
print("-"*30)
print("Exercise 3 : Check the index")

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Enter your name: ")

if user_name in names:
    print(f"{user_name} found at index {names.index(user_name)}")
else:
    print("Name not found.")

# Exercise 4
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

# Exercise 5
print("-"*30)
print("Exercise 5 : Thank You 🙌")
