# Q8. Flight Reservation
# Ek Flight class banao jisme private variable __passengers (list) ho.
# Method add_passenger(name) → passenger add kare.
# Method remove_passenger(name) → passenger delete kare.
# Method show_passengers() → passengers list print kare.


class Flight:
    def __init__(self):
        self.__passengers = []

    def add_passenger(self, name):
        self.__passengers.append(name)

    def remove_passenger(self, name):
        if name in self.__passengers:
            self.__passengers.remove(name)

    def show_passengers(self):
        return self.__passengers


f = Flight()
f.add_passenger("Vikas")
f.add_passenger("Ravi")
f.remove_passenger("Ravi")
print(f.show_passengers())
