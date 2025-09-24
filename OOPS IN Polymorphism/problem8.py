#Q8. Polymorphism with abstract class
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Bark")

Dog().speak()  # Bark

# Logic:

# Abstract method force karta hai subclass ko override karne ke liye
# Explanation:

# Dog ne speak() implement kiya → polymorphic call possible