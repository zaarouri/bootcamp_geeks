first = "hello world"  # Fixed typo from "word" to "world"

# This is a comment.
print("I AM A COMPUTER!")

if 1 < 2 and 4 > 2:
    print("math is fun")

nope = None

result = True and False

length = len("What's my length?")  # Assigned result to a variable if needed

print("I AM SHOUTING!".upper())  # Changed string to uppercase using the instance method

number_as_int = int("1000")  # Convert string "1000" to int

word = "real"
print("4{} ".format(word))

print(3 * "cool")


# kayn chi 7ma9 kay9sm 3la zero
try:
    result = 1 / 0
except ZeroDivisionError as e:
    print(e) 

print("The type of [] is: " + str(type([])))

name = None

name = input("Type your name: ")
print(name)

number = float(input("Enter a number: "))

if number < 0:
    print("That number is less than 0!")
elif number > 0:
    print("That number is greater than 0!")
else:
    print("You picked 0!")

text = "apple"
print(text.index('e'))

text1 = "xylophone"
print(text1.find("y"))

my_string = "hello"
print(my_string.isupper())
