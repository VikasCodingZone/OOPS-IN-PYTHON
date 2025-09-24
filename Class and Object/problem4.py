# Class with Multiple Attributes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 25)
print(p1.name, p1.age)  # Alice 25