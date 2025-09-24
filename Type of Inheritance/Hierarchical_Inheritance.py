# Parent class
class Company:
    def show_company_name(self):
        print("Company: TCS")

# Child1
class HR(Company):
    def show_hr_department(self):
        print("Department: HR")

# Child2
class Developer(Company):
    def show_dev_department(self):
        print("Department: Developer")

# Objects
hr1 = HR()
dev1 = Developer()

hr1.show_company_name()
hr1.show_hr_department()

# dev1.show_company_name()
dev1.show_dev_department()
