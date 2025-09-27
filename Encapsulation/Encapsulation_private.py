class Person:
    def __init__(self,name,age):
        self.__name=name  #__name  double undersqore private variable
        self.__age=age
    
    def display_info(self):
        print(f"The person name is {self.__name} and the age is {self.__age}")

person = Person("vikas",20)
person.display_info()
