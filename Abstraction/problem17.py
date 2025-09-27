# Q17. Food Delivery (Pizza vs Burger)
from abc import ABC, abstractmethod

class Food(ABC):
    @abstractmethod
    def order(self):
        pass

class Pizza(Food):
    def order(self):
        return "Pizza ordered "

class Burger(Food):
    def order(self):
        return "Burger ordered "

f = Pizza()
print(f.order())


# Q17. Food Delivery (Pizza vs Burger)
# Common feature: food order karna.
# Pizza aur Burger order karne ka implementation alag.
# Abstraction se user ko sirf order() method dikhai deta hai.