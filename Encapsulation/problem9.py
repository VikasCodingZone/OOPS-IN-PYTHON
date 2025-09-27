# Q9. Wallet Payment System
# Ek Wallet class banao jisme private variable __balance ho.
# Method add_money(amount) → balance increase kare.
# Method pay(amount) → agar enough balance hai to deduct kare else "Insufficient Balance".
# Method check_balance() → current balance show kare.


class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount

    def pay(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def check_balance(self):
        return self.__balance


w = Wallet(1000)
w.add_money(500)
w.pay(2000)  # Insufficient
print(w.check_balance())
