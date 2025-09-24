# Updating Object Attributes
class Student:
    def __init__(self, name):
        self.name = name

s = Student("John")
s.name = "Mike"
print(s.name)  # Mike