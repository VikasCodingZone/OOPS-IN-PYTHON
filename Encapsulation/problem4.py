# Q4. Library Management
# Ek Library class banao jisme private list __books ho.
# Method add_book(book) → book add kare.
# Method issue_book(book) → agar book available hai to issue karo, otherwise "Not Available".
# Method show_books() → available books print kare.

class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def issue_book(self, book):
        if book in self.__books:
            self.__books.remove(book)
        else:
            print("Not Available")

    def show_books(self):
        return self.__books


lib = Library()
lib.add_book("Python")
lib.add_book("DSA")
lib.issue_book("Python")
print(lib.show_books())
