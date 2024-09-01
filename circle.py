import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_circumference(self):
        return 2 * math.pi * self.radius

# Example usage:
circle = Circle(5)
print("Area:", circle.get_area())
print("Circumference:", circle.get_circumference())
