#Q6. Function with default argument (polymorphism)
def multiply(a, b=1):
    return a * b

print(multiply(5))    # 5
print(multiply(5, 3)) # 15


# Logic:

# Same function different number of arguments handle karta hai
# Explanation:

# multiply(5) → 1 default b ke saath multiply

# multiply(5, 3) → dono values multiply