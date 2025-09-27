# 11. Using Getter Method

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance

account = BankAccount(8000)
print(account.get_balance())

#Logic: Getter method se private data ko read kar sakte hain.