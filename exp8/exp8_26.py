class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("New instance created.")
        return cls._instance

    def show_id(self):
        print("Object id:", id(self))

a = Singleton()
b = Singleton()
print(a is b)   # True — same object
a.show_id()
b.show_id()