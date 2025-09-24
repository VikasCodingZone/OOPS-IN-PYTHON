#Q1. Function polymorphism (same function, different types)
def add(a, b):
    return a + b

print(add(5, 3))        # 8
print(add("Hi ", "Vikas"))  # Hi Vikas



# Logic:

# add() function alag-alag data types (int, str) ke liye kaam karta hai.
# Explanation:

# add(5, 3) → integers add hote hain

# add("Hi ", "Vikas") → strings concatenate hote hain

# Same function, multiple forms → function polymorphism