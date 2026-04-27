import math

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return round(math.pi * self.r ** 2, 2)

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l, self.b = l, b
    def area(self):
        return self.l * self.b

shapes = [Circle(5), Rectangle(4, 6)]
for s in shapes:
    print(type(s).__name__, "area:", s.area())