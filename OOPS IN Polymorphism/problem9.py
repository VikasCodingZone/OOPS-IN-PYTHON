#Q9. Operator overloading (*)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)
    def show(self):
        print(self.x, self.y)

p = Point(2, 3)
(p * 3).show()  # 6 9


# logic:

# * operator ko Point class ke liye customize kiya
# Explanation:

# p * 3 → coordinates multiply ho jaate hain → polymorphism