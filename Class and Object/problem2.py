# Multiple Objects
class Car:
    def __init__(self, model):
        self.model = model

car1 = Car("Honda")
car2 = Car("Toyota")

print(car1.model)  # Honda
print(car2.model)  # Toyota