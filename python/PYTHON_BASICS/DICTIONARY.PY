# Exercise 1: Create dictionary from list of tuples
data = [("name", "Elie"), ("job", "Instructor")]
dict1 = dict(data)
print(dict1)

print("-----------------------")

# Exercise 2: Create dictionary from two lists
states_abbr = ["CA", "NJ", "RI"]
states_full = ["California", "New Jersey", "Rhode Island"]
states_dict = dict(zip(states_abbr, states_full))
print(states_dict)

print("-----------------------")

# Exercise 3: Create dictionary with vowels as keys and 0 as values
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_dict = {vowel: 0 for vowel in vowels}
print(vowels_dict)

print("-----------------------")

# Exercise 4: Create dictionary with alphabet position as key and letter as value
import string
alphabet_dict = {i + 1: letter for i, letter in enumerate(string.ascii_uppercase)}
print(alphabet_dict)

print("-----------------------")

# Super Bonus: Count vowels in "awesome sauce"
text = "awesome sauce"
vowels = "aeiou"
vowel_count = {vowel: text.lower().count(vowel) for vowel in vowels}
print(vowel_count)