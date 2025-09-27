# Q19. Travel Booking (Flight vs Train)
from abc import ABC, abstractmethod

class Travel(ABC):
    @abstractmethod
    def book(self):
        pass

class Flight(Travel):
    def book(self):
        return "Flight ticket booked "

class Train(Travel):
    def book(self):
        return "Train ticket booked "

t = Train()
print(t.book())


# Q19. Travel Booking (Flight vs Train)
# Common feature: ticket booking.
# Flight aur Train booking ka backend system alag hota hai.
# Abstraction: sirf book() method same.