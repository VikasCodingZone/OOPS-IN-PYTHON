#Q19. Method chaining + polymorphism
class Calculator:
    def __init__(self, value=0):
        self.value = value
    def add(self, n):
        self.value += n
        return self
    def multiply(self, n):
        self.value *= n
        return self

c = Calculator()
print(c.add(5).multiply(2).value)  # 10


# Logic:

# Methods ek object return karte hain → chain possible
# Explanation:

# Same methods multiple forms me combine hoke work karte → polymorphism