
# Class Counting Objects
class Student:
    count = 0  # Class variable

    def __init__(self, name):
        self.name = name
        Student.count += 1

s1 = Student("A")
s2 = Student("B")
s3 = Student("C")





