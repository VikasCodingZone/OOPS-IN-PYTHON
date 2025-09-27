# Q18. Encapsulation + Banking
class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, atm):
        if atm > 0:
            self.__balance += atm

    def get_balance(self):
        return self.__balance

b = Bank(1000)
b.deposit(500)
print(b.get_balance())


# Logic: Balance secure hai, sirf methods se update hoga.