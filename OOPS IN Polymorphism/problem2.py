#Q2. Method overriding (dynamic polymorphism)
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof Woof")

d = Dog()
d.speak()  # Woof Woof

# Logic:

# Subclass Dog ne parent class Animal ka speak() method override kiya.
# Explanation:

# Runtime pe Python Dog ka version call karta hai → dynamic polymorphism