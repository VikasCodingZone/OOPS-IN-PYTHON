#Q15. Property with Setter

class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value

item = Product(500)
item.price = 600
print(item.price)


#Logic: Encapsulation ke saath validation aur setter ka use.