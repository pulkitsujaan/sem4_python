from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return round(math.pi * self.r**2, 2)

class Triangle(Shape):
    def __init__(self, b, h): self.b, self.h = b, h
    def area(self): return 0.5 * self.b * self.h

for s in [Circle(7), Triangle(6, 4)]:
    print(type(s).__name__, "->", s.area())