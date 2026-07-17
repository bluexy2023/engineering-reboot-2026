# Exercise 3 of Day 21
# multiple exceptions demo

try:
    first = float(input("First Number: "))
    second = float(input("Second Number:"))
    quotient = first / second
except ValueError:
    print("Invalid input: numbers are required.")
except ZeroDivisionError:
    print("Invalid operation: division by zero not allowed.")
else:
    print(f"Quotient: {quotient}")