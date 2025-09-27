# Q3. Shopping Cart
# Ek Cart class banao jisme private dictionary __items ho.
# Method add_item(name, price) → cart me item add kare.
# Method remove_item(name) → item remove kare.
# Method checkout() → total price return kare.
class Cart:
    def __init__(self):
        self.__items = {}

    def add_item(self, name, price):
        self.__items[name] = price

    def remove_item(self, name):
        if name in self.__items:
            del self.__items[name]

    def checkout(self):
        return sum(self.__items.values())


c = Cart()
c.add_item("Shoes", 1500)
c.add_item("Bag", 2000)
c.remove_item("Shoes")
print(c.checkout())
