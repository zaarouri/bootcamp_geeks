list1 = [1, 2, 3, 4]
for value in list1:
    print(value)

print("-----------------------")

list2 = [1, 2, 3, 4]
for value in list2:
    print(value * 20)

print("-----------------------")

names = ["Elie", "Tim", "Matt"]
first_letters = [name[0] for name in names]
print(first_letters)

print("-----------------------")

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

print("-----------------------")

list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
common_values = [value for value in list_a if value in list_b]
print(common_values)

print("-----------------------")

words = ["Elie", "Tim", "Matt"]
reversed_words = [word[::-1].lower() for word in words]
print(reversed_words)

print("-----------------------")

string1 = "first"
string2 = "third"
common_letters = list(set(string1) & set(string2))
common_letters.sort()
print(common_letters)

print("-----------------------")

divisible_by_12 = [num for num in range(1, 101) if num % 12 == 0]
print(divisible_by_12)

print("-----------------------")

string = "amazing"
vowels = "aeiouAEIOU"
consonants = [char for char in string if char not in vowels]
print(consonants)

print("-----------------------")

list_of_lists = [[0, 1, 2] for _ in range(3)]
print(list_of_lists)

print("-----------------------")

big_list = [[i for i in range(10)] for _ in range(10)]
print(big_list)