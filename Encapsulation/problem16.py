#Q16. Encapsulation in Inheritance

class Car:
    def __init__(self):
        self.__engine = "V8"
    
    def get_engine(self):
        return self.__engine

class BMW(Car):
    pass

b = BMW()
print(b.get_engine())


#Logic: Private data child class ko directly nahi milta.