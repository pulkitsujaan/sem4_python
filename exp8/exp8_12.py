class Vehicle:
    def start(self):
        print("Vehicle started.")

class Car(Vehicle):
    def honk(self):
        print("Car goes beep!")

class ElectricCar(Car):
    def charge(self):
        print("Charging the battery...")

ec = ElectricCar()
ec.start()    # from Vehicle
ec.honk()     # from Car
ec.charge()   # own method