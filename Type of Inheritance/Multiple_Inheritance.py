# Parent classes
class Science:
    def science_marks(self, marks):
        print(f"Science Marks: {marks}")

class Math:
    def math_marks(self, marks):
        print(f"Math Marks: {marks}")

# Child class inherits from both
class SecondaryStudent(Science, Math):
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Secondary School Student: {self.name}")

# Object
s2 = SecondaryStudent("vikas")
s2.show_name()
s2.science_marks(90)
s2.math_marks(95)
