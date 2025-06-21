
# Exercise 1 : Cats 
print("-"*30)
print("Exercise 1 : Cats")
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

# Step 1: Create cat objects
cat1 = Cat("Fluffy", 3)
cat2 = Cat("Whiskers", 2)
cat3 = Cat("Tigger", 5)

# Step 2: Create a function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):
    # ... code to find and return the oldest cat ...
    return max(cat1, cat2, cat3, key=lambda cat: cat.age)

# Step 3: Print the oldest cat's details 
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest_cat.name} and is {oldest_cat.age} years old.")
# Exercise 2 : Dogs
print("-"*30)
print("Exercise 2 : Dogs")
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def bark(self):
        print(f"{self.name}goes woof!")
        
    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")
        
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)
print("Dog 1 - Name:", davids_dog.name, "Height:", davids_dog.height)
davids_dog.bark()
davids_dog.jump()
print("Dog 2 - Name:", sarahs_dog.name, "Height:", sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()
# Exercise 3  : song producer 
print("-"*30)
print("Exercise 3 : song producer")
class Song:
    def __init__(self, lyrics):
        self.lyrics = list(lyrics)
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


print("-" * 30)
print("Exercise 4 : Zoo")

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal in self.animals:
            print("animal already exists")
        else:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold not in self.animals:
            print("animal does not exist")
        else:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()
        grouped = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            grouped.setdefault(first_letter, []).append(animal)
        self.grouped_animals = grouped
        return grouped

    def get_groups(self):
        if hasattr(self, 'grouped_animals'):
            for letter, group in self.grouped_animals.items():
                print(f"{letter}: {group}")
        else:
            print("Please sort animals first using sort_animals().")

# Create and use the zoo
zoo = Zoo("Ramat Gan Safari")
zoo.add_animal("Lion")
zoo.add_animal("Giraffe")
zoo.add_animal("Bear")
zoo.add_animal("Zebra")
zoo.add_animal("Cougar")
zoo.add_animal("Baboon")
zoo.add_animal("Cat")
zoo.add_animal("Lion")        # duplicate
zoo.get_animals()
zoo.sell_animal("Tiger")      # not in list
zoo.get_animals()
zoo.get_groups()    
Zoo.sort_animals(zoo)  # Call sort_animals()       

