7# Class with Default Values
class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

b1 = Book("Python Basics")
b2 = Book("AI Handbook", "Dr. Smith")

print(b1.author)  # Unknown
print(b2.author)  # Dr. Smith