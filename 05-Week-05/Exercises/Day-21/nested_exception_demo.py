# Exercise 7 of Day 21
# nested_exception_demo.py
# Combine validation loops and exception handling 
# to build a resilient input workflow.

def read_number(prompt: str) -> float:
    while True:
        try:
            # if float() conversion of an input 
            # trows a ValueError exception
            # will be caught by the next except block
            # else, it will return the float value of the 
            # input and exit the loop, and the function
            return float(input(prompt)) 
        except ValueError:
            # this block gets executed if there was a ValueError
            # exeption above.  then the loop continues
            print("Invalid number. Please try again.")


first = read_number("First number: ")
second = read_number("Second number: ")

try: 
    result = first / second
except ZeroDivisionError: 
    print("Cannot divide by zero.")
else: 
    print(f"Result: {result}")