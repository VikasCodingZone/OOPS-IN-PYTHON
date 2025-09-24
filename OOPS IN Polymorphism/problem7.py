#Q7. Polymorphism using inheritance
class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

s = Square(4)
print(s.area())  # 16

# Logic:

# Base class me generic method, subclass me specific implementation
# Explanation:

# Square class ne area() override kiya → run-time polymorphism