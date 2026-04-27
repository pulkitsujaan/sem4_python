class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # getter
    def get_name(self): return self.__name
    def get_age(self):  return self.__age

    # setter
    def set_name(self, name): self.__name = name
    def set_age(self, age):
        if age < 0:
            print("Age cannot be negative.")
        else:
            self.__age = age

p = Person("Dave", 25)
print(p.get_name(), p.get_age())
p.set_age(30)
print(p.get_age())
p.set_age(-5)