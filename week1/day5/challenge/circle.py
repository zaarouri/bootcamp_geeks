import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius:
            self.radius = radius
        elif diameter:
            self.radius = diameter / 2
        else:
            raise ValueError("Please provide either radius or diameter.")

    def get_radius(self):
        return self.radius

    def get_diameter(self):
        return self.radius * 2

    def get_area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius:.2f}"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius
c1 = Circle(radius=3)
c2 = Circle(diameter=10)

print(c1)                            # Circle with radius 3.00
print("Radius:", c2.get_radius())   # 5.0
print("Diameter:", c1.get_diameter())  # 6.0
print("Area:", c1.get_area())       # 28.27...

c3 = c1 + c2
print(c3)                            # Circle with radius 8.00

print(c1 == c2)                      # False
print(c1 < c2)                       # True

# Sort example
circles = [c2, c3, c1]
sorted_circles = sorted(circles)
for c in sorted_circles:
    print(c)
