# Q2. Vehicle (Car vs Bike)

# Logic: Vehicle ka drive function har jagah alag.
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Driving a car "

class Bike(Vehicle):
    def drive(self):
        return "Riding a bike "

v = Bike()
print(v.drive())


# Q2. Vehicle (Car vs Bike)
# Dono vehicles ka kaam hai drive() karna.
# Car aur Bike ki driving process alag hoti hai.
# Abstraction se user ko sirf drive() button milega, details hide rahengi.

