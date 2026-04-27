class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, o):
        return Vector(self.x + o.x, self.y + o.y)

    def __sub__(self, o):
        return Vector(self.x - o.x, self.y - o.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 4)
print(v1 + v2)     # (3, 7)
print(v1 - v2)     # (1, -1)
print(v1 * 3)      # (6, 9)