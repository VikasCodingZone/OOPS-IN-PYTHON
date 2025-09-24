# Parent class
class PrimarySchool:
    def __init__(self, student_name):
        self.student_name = student_name

    def show_name(self):
        print(f"Primary School Student: {self.student_name}")

# Child class
class PrimaryStudent(PrimarySchool):
    def show_grade(self, grade):
        print(f"Grade: {grade}")

# Object
s1 = PrimaryStudent("Vikas")
s1.show_name()
s1.show_grade("5th")
