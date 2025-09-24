#Q4. Polymorphism with list of objects
class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

for animal in [Dog(), Cat()]:
    animal.speak()


# Logic:

# Loop me multiple objects ke liye same method call kiya.
# Explanation:

# Har object apna speak() execute karta → polymorphism