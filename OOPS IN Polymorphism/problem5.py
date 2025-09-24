#Q5. Duck typing example
class Car:
    def drive(self):
        print("Car is driving")

class Bike:
    def drive(self):
        print("Bike is driving")

def start(vehicle):
    vehicle.drive()

start(Car())
start(Bike())


# Function sirf check karta hai ki object drive() method rakhta hai ya nahi.
# Explanation:

# Car() aur Bike() dono ke liye same function kaam karta → duck typing