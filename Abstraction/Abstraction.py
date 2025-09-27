# Definition: Abstraction ka matlab hai sirf essential features dikhana 
# aur implementation details ko hide karna (means process ko hide karna ...)
#ex - ATM se pese nikalna (hume pese nikalne se matlb hai
#  andar kese kya process huva use se nahi..)
# Python me abstraction ko achieve karne ke liye abc module ka use hota hai
# jisme ABC (Abstract Base Class) aur @abstractmethod decorator use kiya jata hai.


from abc import ABC, abstractmethod

# Abstract Class
class Payment(ABC):
    @abstractmethod   #  @abstractmethod ye method jaha likhi ho vo abstract class hoti hai
    def pay(self, amount):
        pass   # only method structure, no body


# Concrete Class 1
class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} using Credit Card"


# Concrete Class 2
class UpiPayment(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} using UPI"


# Using abstraction
payment1 = CreditCardPayment()
print(payment1.pay(1000))

payment2 = UpiPayment()
print(payment2.pay(500))






































