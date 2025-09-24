# Base class
class PrimarySchool:
    def show_primary(self):
        print("Primary School: Govt.boys high School")

# Parent1
class SecondarySchool(PrimarySchool):
    def show_secondary(self):
        print("Secondary School:  Govt.boys high Secondary School")

# Parent2
class College:
    def show_college(self):
        print("College: SD Bansal College")

# Child class inherits from both (Hybrid)
class StudentHybrid(SecondarySchool, College):
    def show_name(self, name):
        print(f"Student Name: {name}")

# Object
student = StudentHybrid()
student.show_primary()    # From PrimarySchool
student.show_secondary()  # From SecondarySchool
student.show_college()    # From College
student.show_name("Vikas")
