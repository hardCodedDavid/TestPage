import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def circumference(self):
        return 2 * math.pi * self.radius
        
c = Circle(5)

print("The area of the circle is:", c.area())

print("The circumference of the circle is:", c.circumference())
