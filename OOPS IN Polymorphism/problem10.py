#Q10. Method overloading simulation using args
class Calculator:
    def add(self, *args):
        return sum(args)

c = Calculator()
print(c.add(2, 3))       # 5
print(c.add(1, 2, 3, 4)) # 10



# Logic:

# *args variable number of arguments allow karta hai
# Explanation:

# add(2,3) ya add(1,2,3,4) dono kaam karta → pseudo-polymorphism