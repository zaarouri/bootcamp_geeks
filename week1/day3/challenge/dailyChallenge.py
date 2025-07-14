class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        result = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            result += f"{animal} : {count}\n"
        result += "\n    E-I-E-I-0!"
        return result

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        types = self.get_animal_types()
        animals_str = ""
        for i in range(len(types)):
            animal = types[i]
            name = animal + "s" if self.animals[animal] > 1 else animal
            if i == len(types) - 1 and len(types) > 1:
                animals_str += "and " + name
            elif i == len(types) - 1:
                animals_str += name
            else:
                animals_str += name + ", "
        return f"{self.name}'s farm has {animals_str}."
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print()
print(macdonald.get_short_info())
