class UpperMeta(type):
    """Converts all method names to uppercase."""
    def __new__(mcs, name, bases, namespace):
        upper_ns = {}
        for k, v in namespace.items():
            if not k.startswith("_"):
                upper_ns[k.upper()] = v
            else:
                upper_ns[k] = v
        return super().__new__(mcs, name, bases, upper_ns)

class MyClass(metaclass=UpperMeta):
    def hello(self):
        print("Hello from hello!")

obj = MyClass()
obj.HELLO()   # method name transformed to uppercase