# Exercise 4 of Day 21
# try else demo
# Use else to separate success-path logic 
# from exception handling logic.

try:
    age = int(input("Enter age: "))
except ValueError:
    print("Age must be a whole number")
else:
    print(f"Age accepted: {age}")