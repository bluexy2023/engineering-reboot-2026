# Exercise 2 of Day 21
# Perform division safely 
# and recover when the denominator is zero.

try: 
    numerator = float(input("Enter numerator: ")) 
    denominator = float(input("Enter denominator: ")) 
    result = numerator / denominator 
    print(f"Result: {result}")
except ValueError: 
    print("Both values must be numeric.")
except ZeroDivisionError: 
    print("Cannot divide by zero.")