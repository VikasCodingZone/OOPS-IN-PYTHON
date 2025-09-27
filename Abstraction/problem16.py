# Q16. Ride Booking (Uber vs Ola)
from abc import ABC, abstractmethod

class RideApp(ABC):
    @abstractmethod
    def book_ride(self, location):
        pass

class Uber(RideApp):
    def book_ride(self, location):
        return f"Ride booked on Uber to {location}"

class Ola(RideApp):
    def book_ride(self, location):
        return f"Ride booked on Ola to {location}"

r = Ola()
print(r.book_ride("Indore"))


# Q16. Ride Booking (Uber vs Ola)
# Common feature: ride book karna.
# Uber aur Ola ka backend fare calculation + allocation process alag hota hai.
# User ko sirf book_ride(location) dikhai deta hai.