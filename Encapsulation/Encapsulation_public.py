class Person:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    
    def display_info(self):
        print(f"The person name is {self.name} and the age is {self.age}")

person = Person("vikas",20)
person.display_info()