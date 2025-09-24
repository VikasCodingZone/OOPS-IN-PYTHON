#Q15. Polymorphism using multiple classes and common method
class Dog:
    def sound(self):
        print("Woof")
class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

for a in [Dog(), Cat()]:
    make_sound(a)


#     Logic:

# Function kisi bhi class ke object ke liye call hota
# Explanation:

# Dog() aur Cat() dono sound() provide karte → polymorphic behavior