class Person:
    def __init__(self,name,age):
        self._name=name  #__name  single  undersqore private variable
        self._age=age
    

class Student(Person ):
    def __init__(self,name,age):
        super().__init__(name,age)

    def display_info(self):
        print(f"The person name is {self._name} and the age is {self._age}") 

student1= Student("vikas",20)   
student1.display_info()        