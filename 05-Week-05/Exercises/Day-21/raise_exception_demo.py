# exercise 6 of day 21
# raise_exception.py
# Raise ValueError intentionally when 
# a business rule is violated.

def validate_age(age: int) -> None: 
    if age < 0: 
        raise ValueError("Age cannot be negative.")

try: 
    age = int(input("Enter age: ")) 
    validate_age(age)
except ValueError as error: 
    print(f"Invalid age: {error}")
else: 
    print(f"Age accepted: {age}")