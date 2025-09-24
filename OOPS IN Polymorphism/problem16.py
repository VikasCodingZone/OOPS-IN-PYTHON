# Q16. Polymorphism with custom exceptions
class MyError(Exception):
    def __str__(self):
        return "This is a custom error"

try:
    raise MyError()
except MyError as e:
    print(e)

#     Logic:

# Function kisi bhi class ke object ke liye call hota
# Explanation:

# Dog() aur Cat() dono sound() provide karte → polymorphic behavior