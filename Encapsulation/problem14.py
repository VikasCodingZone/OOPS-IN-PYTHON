#14 Using @property Decorator

class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        return self.__price

item = Product(200)
print(item.price)


#Logic: Getter ko short form me @property se likhte hain.
