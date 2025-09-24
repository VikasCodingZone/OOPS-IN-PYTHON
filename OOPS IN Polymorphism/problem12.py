#Q12. Overriding __str__ method
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Person: {self.name}"

p = Person("Vikas")
print(p)  # Person: Vikas

# Logic:

# Object print karte waqt custom string output
# Explanation:

# print(p) → automatic __str__() call → polymorphic behavior