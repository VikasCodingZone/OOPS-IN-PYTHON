
8#Class with Return Value
class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
result = calc.add(10, 5)
print(result)  # 15