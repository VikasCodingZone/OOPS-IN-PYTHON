# 2 Bank Loan System
#  Ek LoanAccount class banao jisme private variable __loan_amount ho.
# Method take_loan(amount) → loan amount add kare.
# Method repay(amount) → loan repay kare. Agar repay > loan hai to "Extra repayment not allowed".
# Method get_loan_balance() se remaining loan show ho.

class LoanAccount:
    def __init__(self, name):
        self.__name = name
        self.__loan_amount = 0

    def take_loan(self, amount):
        if amount > 0:
            self.__loan_amount += amount

    def repay(self, amount):
        if amount <= self.__loan_amount:
            self.__loan_amount -= amount
        else:
            print("Extra repayment not allowed")

    def get_loan_balance(self):
        return self.__loan_amount


loan = LoanAccount("Amit")
loan.take_loan(5000)
loan.repay(2000)
loan.repay(4000)  # Invalid
print(loan.get_loan_balance())
