1# Simple Class & Object
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} is barking")

dog1 = Dog("Tommy")
dog1.bark()  # Output: Tommy is barking