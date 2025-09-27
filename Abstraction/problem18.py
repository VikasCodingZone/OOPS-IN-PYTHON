# Q18. Bank Loan (Home Loan vs Car Loan)

from abc import ABC, abstractmethod
class Loan(ABC):
    @abstractmethod
    def get_interest_rate(self):
        pass

class HomeLoan(Loan):
    def get_interest_rate(self):
        return "Home Loan interest rate: 8%"

class CarLoan(Loan):
    def get_interest_rate(self):
        return "Car Loan interest rate: 10%"

l = CarLoan()
print(l.get_interest_rate())


# Q18. Bank Loan (Home Loan vs Car Loan)
# Common kaam: loan lena.
# Lekin Home loan aur Car loan ke interest rates alag.
# Abstraction: user sirf get_interest_rate() call karega.