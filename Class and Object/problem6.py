6# Object Interaction
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"{self.name} earns {self.salary}")

e1 = Employee("Sam", 5000)
e2 = Employee("Ann", 7000)

for emp in (e1, e2):
    emp.display()
