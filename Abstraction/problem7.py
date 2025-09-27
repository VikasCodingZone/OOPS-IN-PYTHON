# Q7. Animal Sound (Dog, Cat)
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof 🐶"

class Cat(Animal):
    def sound(self):
        return "Meow 🐱"

a = Cat()
print(a.sound())


# Q7. Animal Sound (Dog, Cat)
# Har animal sound karta hai, but sound alag hoti hai.
# Common function: sound().
# Dog → Woof, Cat → Meow.
# User ko sirf sound() call karna hai, detail hidden.