class MathOperations:
    pi = 3.14159

    def instance_method(self, x):
        # has access to self (instance)
        return x * 2

    @classmethod
    def class_method(cls, r):
        # has access to cls (class)
        return cls.pi * r * r

    @staticmethod
    def static_method(a, b):
        # no access to self or cls
        return a + b

m = MathOperations()
print(m.instance_method(5))          # 10
print(MathOperations.class_method(3))# 28.27...
print(MathOperations.static_method(4, 6)) # 10