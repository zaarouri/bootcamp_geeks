#Exercise 1: What is the Season?
month = int(input("Enter a month number (1 to 12): "))

if month in [3, 4, 5]:
    print("It's Spring!")
elif month in [6, 7, 8]:
    print("It's Summer!")
elif month in [9, 10, 11]:
    print("It's Autumn!")
elif month in [12, 1, 2]:
    print("It's Winter!")
else:
    print("Invalid month.")
#Exercise 2: For Loop
for i in range(1, 21):
    print(i)

print("Numbers at even index positions:")
for i in range(1, 21):
    if (i - 1) % 2 == 0:
        print(i)    
#Exercise 3: While Loop
my_name = "Abdelmounime"

while True:
    name = input("Enter your name: ")
    if name.strip().lower() == my_name.lower():
        print("That's my name too!")
        break
#Exercise 4: Check the index
names = ['abdelmounime', 'marouan', 'salma', 'yassmine', 'adnane', 'anas']
user_name = input("Enter your name: ")

if user_name in names:
    print(f"{user_name} is found at index {names.index(user_name)}.")
else:
    print("Name not found.")
#Exercise 5: Greatest Number
num1 = int(input("Input the 1st number: "))
num2 = int(input("Input the 2nd number: "))
num3 = int(input("Input the 3rd number: "))

greatest = max(num1, num2, num3)
print(f"The greatest number is: {greatest}")


#Exercise 6: Random Number
import random

wins = 0
losses = 0

while True:
    guess = input("Guess a number (1-9) or type 'quit' to exit: ")

    if guess.lower() == 'quit':
        break

    if not guess.isdigit() or not (1 <= int(guess) <= 9):
        print("Invalid input. Enter a number between 1 and 9.")
        continue

    guess = int(guess)
    number = random.randint(1, 9)
    print(f"The random number was: {number}")

    if guess == number:
        print("Winner!")
        wins += 1
    else:
        print("Better luck next time.")
        losses += 1

print(f"\nGames played: {wins + losses}")
print(f"Wins: {wins}")
print(f"Losses: {losses}")
