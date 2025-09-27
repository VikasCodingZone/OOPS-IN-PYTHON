# Q6. ATM Simulation
# Ek ATM class banao jisme private variables __pin aur __balance ho.
# Method check_pin(pin) → agar correct pin hai to hi balance show ho.
# Method deposit(pin, amt) aur withdraw(pin, amt) implement karo.

class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def check_pin(self, pin):
        return pin == self.__pin

    def deposit(self, pin, amt):
        if self.check_pin(pin):
            self.__balance += amt
        else:
            print("Wrong PIN")

    def withdraw(self, pin, amt):
        if self.check_pin(pin):
            if amt <= self.__balance:
                self.__balance -= amt
            else:
                print("Insufficient Balance")
        else:
            print("Wrong PIN")

    def get_balance(self, pin):
        if self.check_pin(pin):
            return self.__balance
        else:
            return "Access Denied"


atm = ATM(1234, 5000)
atm.deposit(1234, 2000)
atm.withdraw(1111, 1000)  # Wrong PIN
print(atm.get_balance(1234))
