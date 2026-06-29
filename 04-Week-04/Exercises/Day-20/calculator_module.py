# calculator_module 
# similar to math_utils, but we'll design it in such a way 
# that we'll throw an exception for invalid input
# i.e, division by zero

# add function
def add(a,b):
    return a + b

# subtract function
def subtract(a,b):
    return a - b

# multiply function
def multiply(a,b):
    return a * b

# def divide(a,b):
def divide(a,b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

# power function
def power(a,b):
    # python exponentation is **
    return a ** b

# modulus function
# returns the remainder of the division
# ex. 5 % 3 = 2
def modulus(a,b):
    # python modulus operator %
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a % b

# floor_division function
# returns the division rounded down to its nearest integer 
# floor division operator is //
def floor_division(a,b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a // b

