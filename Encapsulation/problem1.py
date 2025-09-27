# Q1. Student Marks System
#  Ek Student class banao jisme private variable __marks ho.
# Method add_marks(subject, marks) se marks add karo.
# Method get_marks() se dictionary return ho.
# Agar marks 0–100 ke beech nahi hain to "Invalid Marks" print ho.
class Student:
    def __init__(self, name):
        self.__name = name
        self.__marks = {}

    def add_marks(self, subject, marks):
        if 0 <= marks <= 100:
            self.__marks[subject] = marks
        else:
            print("Invalid Marks")

    def get_marks(self):
        return self.__marks


s = Student("Vikas")
s.add_marks("Math", 90)
s.add_marks("English", 105)  # Invalid
print(s.get_marks())
