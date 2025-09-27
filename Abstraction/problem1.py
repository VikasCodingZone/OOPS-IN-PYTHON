# Q1. Payment System (Card vs UPI)

# Logic: Different payment methods, user ko detail ka nahi pata.

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} using Credit Card"

class UpiPayment(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} using UPI"

payment = UpiPayment()
print(payment.pay(500))


# User ko bas pay() method dikh raha hai, implementation alag hai.


# Q1. Payment System (Card vs UPI)
# Har payment ka method same hai → pay(amount)
# Lekin implementation alag hoga: card ke liye card process, UPI ke liye UPI gateway.
# User ko bas pay() dikhai deta hai.