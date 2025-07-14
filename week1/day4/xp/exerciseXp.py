#Exercise 1: Pets
print("-"*30)
print("Exercise 1 : Pets")
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

# Step 1: Define Bengal and Chartreux breeds
class Bengal(Cat):
    def sing(self, sounds):
        return f'{self.name} says {sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{self.name} says {sounds}'


class Siamese(Cat):
    def __init__(self, name, age, eye_color):
        super().__init__(name, age)
        self.eye_color = eye_color  

    def purr(self):
        return f'{self.name} is purring with its {self.eye_color} eyes'

    def sing(self, sounds):
        return f'{self.name} sings {sounds} with elegance'

cat1 = Bengal("Leo", 3)
cat2 = Chartreux("Misty", 5)
cat3 = Siamese("Suki", 2, "blue")

all_cats = [cat1, cat2, cat3]

sara_pets = Pets(all_cats)


sara_pets.walk()

 # Exercise 2: Dogs
print("-"*30)
print("Exercise 2 : Dogs")
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark (self):
        print(f"{self.name} is barking ")
    def run_speed (self):
        speed = self.weight / self.age * 10
        return speed
    def fight(self, other_dog):
        if self.run_speed()*self.weight > other_dog.run_speed()*other_dog.weight:
            return f"{self.name} wins the fight"
        else:
            return f"{other_dog.name} wins the fight"

dog1 = Dog("Buddy", 3, 10)
dog2 = Dog("Max", 4, 12)

dog1.bark()
dog2.bark()

print(dog1.fight(dog2))
# Exercise 3: Dogs Domesticated
print("-"*30)
print("Exercise 3 : Dogs Domesticated")

# the exercise require to use the Dog class from the previous exercise in other file so i have to create a new file named exercise3.py



# Exercise 4: Family and Person Classes
print("-"*30)
print("Exercise 4 : Family and Person Classes")
class Person :
    def __init__(self, first_Name,  last_Name, age):
        self.first_Name = first_Name
        self.last_Name = last_Name
        self.age = age
    def is_18 (self):
       return self.age >= 18

class Family:
    def __init__(self, family_name):
        self.family_name = family_name
        self.members = []
    def born(self,first_name, age):
        member = Person(first_name , self.family_name, age)
        member.last_Name = self.family_name
        self.members.append(member)
        return member
    def check_majority(self,first_name):
        for member in self.members:
            if member.first_Name == first_name:
                if member.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
    def family_presentation(self):
        print(f"Family name: {self.family_name}")
        for member in self.members:
            print(f"Name: {member.first_Name} {member.last_Name}, Age: {member.age}")
            
    # Create a family
smith_family = Family("Smith")

# Add members
smith_family.born("Alice", 16)
smith_family.born("Bob", 20)

# Check if each can go out
smith_family.check_majority("Alice")  # Not allowed
smith_family.check_majority("Bob")    # Allowed

# Show family presentation
smith_family.family_presentation()