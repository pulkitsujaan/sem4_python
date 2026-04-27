def log_methods(cls):
    for attr_name in dir(cls):
        if attr_name.startswith("_"):
            continue
        attr = getattr(cls, attr_name)
        if callable(attr):
            def make_logged(fn):
                def wrapper(*args, **kwargs):
                    print(f"Calling: {fn.__name__}")
                    return fn(*args, **kwargs)
                return wrapper
            setattr(cls, attr_name, make_logged(attr))
    return cls

@log_methods
class Calculator:
    def add(self, a, b): return a + b
    def mul(self, a, b): return a * b

c = Calculator()
print(c.add(2, 3))
print(c.mul(4, 5))