# Q5. Employee Salary Management
# Ek Employee class banao jisme private variable __salary ho.
# Method set_salary(amount) → agar amount > 0 hai tabhi salary update ho.
# Method apply_bonus(percent) → salary me percent bonus add ho.
# Method get_salary() → salary return kare.

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount

    def apply_bonus(self, percent):
        if percent > 0:
            self.__salary += self.__salary * percent / 100

    def get_salary(self):
        return self.__salary


emp = Employee("Ravi", 30000)
emp.apply_bonus(10)
print(emp.get_salary())
