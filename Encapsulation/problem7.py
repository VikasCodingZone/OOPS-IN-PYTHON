# Q7. Movie Ticket Booking
# Ek Movie class banao jisme private variable __seats ho.
# Method book_seat(num) → agar seats available hain to booking kar do, warna "Not Enough Seats".
# Method get_seats() → remaining seats return kare.


class Movie:
    def __init__(self, total_seats):
        self.__seats = total_seats

    def book_seat(self, num):
        if num <= self.__seats:
            self.__seats -= num
        else:
            print("Not Enough Seats")

    def get_seats(self):
        return self.__seats


m = Movie(50)
m.book_seat(10)
m.book_seat(45)  # Invalid
print(m.get_seats())
