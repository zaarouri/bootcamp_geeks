from exerciseXp import Dog
import random
class PetDog(Dog):

    trained = False
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        trained = False
    def train (self):
        super().bark()
        self.trained = True
    def play(self ,*args):
        print(f"{self.name} {args } all play togheter ")
    def do_a_trick(self):
        tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        if self.trained == True:
            trick = random.choice(tricks)
            print(f"{self.name} does {trick}")
        else:
            print(f"{self.name} is not trained yet")
# Test PetDog methods
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.play("Buddy", "Max")
my_dog.do_a_trick()


