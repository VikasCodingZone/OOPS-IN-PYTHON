# Q9. Online Order (Zomato vs Swiggy)
from abc import ABC, abstractmethod

class OrderApp(ABC):
    @abstractmethod
    def place_order(self, item):
        pass

class Zomato(OrderApp):
    def place_order(self, item):
        return f"Ordered {item} via Zomato"

class Swiggy(OrderApp):
    def place_order(self, item):
        return f"Ordered {item} via Swiggy"

o = Zomato()
print(o.place_order("Pizza"))

# Q9. Online Order (Zomato vs Swiggy)
# User ko khana order karna hai.
# Order ka function place_order(item) sabke liye same hai.
# Lekin backend process Zomato aur Swiggy ka alag hota hai.


