#Q3. Operator overloading (+ operator)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def show(self):
        print(self.x, self.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
(p1 + p2).show()  # 4 6

# Logic:

# + operator ko custom behavior diya Point class ke liye.
# Explanation:

# p1 + p2 → coordinates ka addition → ek naya Point object return