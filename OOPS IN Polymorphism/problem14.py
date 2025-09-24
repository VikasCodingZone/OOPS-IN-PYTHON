#Q14. Dynamic method call using getattr
class Math:
    def add(self, a, b):
        print(a + b)
    def multiply(self, a, b):
        print(a * b)

m = Math()
for method in ["add", "multiply"]:
    getattr(m, method)(5, 3)


#     Logic:

# Method name runtime pe decide hota hai
# Explanation:

# add() ya multiply() call hota → polymorphism
