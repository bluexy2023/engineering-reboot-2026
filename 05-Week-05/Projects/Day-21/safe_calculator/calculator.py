# calculator module that 
# implements the add(), subtract(), multiply(), 
# and divide() functions
# let's assume that validation of the parameters
# have already been enforced by the caller, hence a:float, b:float
# also, all this functions returns a float, thus, ->float:

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b