# Exercise 1: Add Two Numbers
def add_two_numbers(a, b):
    return a + b

# Testing it out
print(add_two_numbers(3, 5))  
print(add_two_numbers(10, 20))


# Exercise 2: Print a Greeting  
def greet(name):
    print(f"Hello, {name}!")

# Let's try it
greet("Alice")
greet("Bob")


# Exercise 3: Check if Number is Even or Odd
def check_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd(4)  # This should print "Even"
check_even_odd(7)  # This should print "Odd"


# Exercise 4: Sum of Numbers in a List
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_list([1, 2, 3, 4]))  
print(sum_list([5, 5, 5]))   


# Exercise 5: Print Days of the Week
def print_days():
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", 
            "Thursday", "Friday", "Saturday"]
    for day in days:
        print(day)

print_days()


# Exercise 6: Check if Number is Positive, Negative, or Zero
def check_sign(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

check_sign(10)  
check_sign(-5)   
check_sign(0)  


# Exercise 7: Repeat a Word
def repeat_word(word, times):
    for i in range(times):
        print(word)

repeat_word("hello", 3)
print() 
repeat_word("goodbye", 2)