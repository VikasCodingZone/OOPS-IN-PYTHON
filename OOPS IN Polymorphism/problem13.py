#Q13. Polymorphism with multiple methods
class Printer:
    def print(self, data):
        print(data)

printer = Printer()
for item in [123, "Hello", [1,2,3]]:
    printer.print(item)


#     Logic:

# Same method print() different data types ke liye kaam karta
# Explanation:

# Dynamic polymorphism + duck typing