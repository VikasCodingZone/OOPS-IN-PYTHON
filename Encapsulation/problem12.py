# 12. Using Setter Method

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount

account = BankAccount(10000)
account.set_balance(12000)
print(account._BankAccount__balance)  # (Name Mangling)


#Logic: Setter method controlled update deta hai.