import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# Get radius from user input
r = int(input("Enter radius of circle: "))

# Create an instance of Circle
obj = Circle(r)

# Print area and perimeter of the circle
print("Area of circle:", round(obj.area(), 2))
print("Perimeter of circle:", round(obj.perimeter(), 2))
