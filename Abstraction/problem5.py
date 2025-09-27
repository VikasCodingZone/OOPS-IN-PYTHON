# Q5. Employee Salary (Full-time, Part-time)
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 50000

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 20000

e = PartTimeEmployee()
print("Salary:", e.calculate_salary())


# Q5. Employee Salary (Full-time, Part-time)
# Salary calculate karna ek common function hai.
# Lekin full-time employee aur part-time employee ke salaries alag hote hain.
# User ko sirf calculate_salary() dikh raha hai, internal rule chhupa hua hai.