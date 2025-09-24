# Grandparent
class School:
    def show_school_name(self):
        print("School: Govt.boys high Sec. School")

# Parent
class College(School):
    def show_college_name(self):
        print("College: SD Bansal College")

# Child
class University(College):
    def show_university_name(self):
        print("University: RGPV University")

# Object
u1 = University()
u1.show_school_name()
u1.show_college_name()
u1.show_university_name()
