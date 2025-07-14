# Exercise 1 : Geometry
print("-"*30)
print("Exercise 1 : Geometry")
import math
class Circle :
    def __init__(self, radius=1.0):
        self.radius = radius
    def get_perimeter(self):
        return (2 * math.pi * self.radius)
    def get_surface(self):
        return (math.pi * math.pow(self.radius, 2))
    def geometrical_definition(self):
        return f"The perimeter of the circle is {self.get_perimeter()} and the surface is {self.get_surface()}"
        
circle = Circle(5)
print(circle.geometrical_definition())   
# Exercise 2 : Custom List Class
print("-"*30)
print("Exercise 2 : Custom List Class")
import random
class MyList :
    def __init__(self, list):
        self.list = list
    def reverse(self):
        reversed_list = self.list[::-1]
        return reversed_list 
    def sort(self):
        self.list = sorted(self.list)
    
    @classmethod
    def construct(cls, length):
        random_list = [random.randint(1, 100) for _ in range(length)]
        return cls(random_list)  # returns an instance of MyList
    def show_list(self):
        print(self.list) 
    
list1 =MyList(['d', 'h', 'c', 'd', 'e'])
list1.show_list()
list1.reverse()
list1.show_list()
list1.sort()
list1.show_list()

list2 = MyList.construct(10)
list2.show_list()



# Exercise 3 : Menu
print("-"*30)
print("Exercise 3 : Menu")
class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice_level": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice_level": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice_level": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice_level": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice_level": "B", "gluten": True}
        ]

    def add_item(self, name, price, spice, gluten):
        self.menu.append({
            "name": name,
            "price": price,
            "spice_level": spice,
            "gluten": gluten
        })
        print(f"{name} added to the menu.")

    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                dish["price"] = price
                dish["spice_level"] = spice
                dish["gluten"] = gluten
                print(f"{name} updated successfully.")
                return
        print(f"{name} not found in the menu.")

    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                self.menu.remove(dish)
                print(f"{name} removed from the menu.")
                return
        print(f"{name} not found in the menu.")

    def show_menu(self):
        for dish in self.menu:
            print(dish)
if __name__ == "__main__":
    manager = MenuManager()

    print("Initial menu:")
    manager.show_menu()

    print("\nAdding Pizza...")
    manager.add_item("Pizza", 20, "B", True)

    print("\nUpdating Soup...")
    manager.update_item("Soup", 12, "C", True)

    print("\nRemoving Salad...")
    manager.remove_item("Salad")

    print("\nFinal menu:")
    manager.show_menu()
        