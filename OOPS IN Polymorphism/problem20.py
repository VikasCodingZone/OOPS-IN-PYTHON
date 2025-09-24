
#Q20. Real-world example: polymorphic shapes
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

shapes = [Rectangle(3,4), Circle(5)]
for shape in shapes:
    print(shape.area())


#     Logic:

# Rectangle aur Circle dono ka area() method call
# Explanation:

# Same interface multiple forms → classic polymorphism