class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real,
                             self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(1, 4)
print(c1 + c2)   # 3 + 7i