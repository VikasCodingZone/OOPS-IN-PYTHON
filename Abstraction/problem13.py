# Q13. ATM Machine (Deposit vs Withdraw)
from abc import ABC, abstractmethod

class ATM(ABC):
    @abstractmethod
    def transaction(self, amount):
        pass

class Deposit(ATM):
    def transaction(self, amount):
        return f"Deposited ₹{amount}"

class Withdraw(ATM):
    def transaction(self, amount):
        return f"Withdrew ₹{amount}"

a = Withdraw()
print(a.transaction(2000))



# Q13. ATM Machine (Deposit vs Withdraw)
# Common interface: transaction(amount).
# Deposit aur Withdraw ke backend steps alag.
# Abstraction se user ko sirf ek button dikhai deta hai.