# Q17. Encapsulation with Salary Hike

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def hike(self, percent):
        if 0 < percent <= 50:
            self.__salary += self.__salary * percent/100
        return self.__salary

e = Employee(30000)
print(e.hike(20))

# Logic: Validation ke saath salary update.