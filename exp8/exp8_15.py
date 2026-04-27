class Dog:
    def sound(self): print("Woof!")

class Cat:
    def sound(self): print("Meow!")

class Cow:
    def sound(self): print("Moo!")

animals = [Dog(), Cat(), Cow()]
for a in animals:
    a.sound()   # same call, different behaviour