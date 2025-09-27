# Q3. Shape Area (Circle, Rectangle)

# Logic: Shapes ka area formula har jagah different.

import math
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self):
        return math.pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self, l, b): self.l, self.b = l, b
    def area(self):
        return self.l * self.b

c = Circle(5)
print("Circle area:", c.area())


# Q3. Shape Area (Circle, Rectangle)
# Har shape ka area() calculate hota hai, but formula alag.
# Circle ke liye πr², rectangle ke liye l × b.
# User ko bas area() call karna hai, formula chhup gaya.