class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def speak(self):               # override
        print(f"{self.name} says: Woof!")

    def fetch(self):
        print(f"{self.name} fetches the ball!")

d = Dog("Bruno")
d.speak()
d.eat()
d.fetch()