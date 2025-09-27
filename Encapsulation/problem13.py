# 13. Name Mangling

class Bank:
    def __init__(self):
        self.__pin = 1234

bank = Bank()
print(bank._Bank__pin)   # Hack way

#Logic: Private data actually _ClassName__variable ke naam se store hota hai.