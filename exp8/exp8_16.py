class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine ({self.horsepower}hp) started.")

class Car:
    def __init__(self, brand, hp):
        self.brand  = brand
        self.engine = Engine(hp)   # composition

    def drive(self):
        self.engine.start()
        print(f"{self.brand} is moving.")

c = Car("Toyota", 150)
c.drive()