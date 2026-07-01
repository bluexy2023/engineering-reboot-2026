# Mini Project - Validated Registration System

# Engineering scenario: Build a console-based employee
# registration workflow that prevents invalid information 
# from entering the system.

## Constants ##
MINIMUM_AGE = 18
MAXIMUM_AGE = 65
MINIMUM_NAME_LENGTH = 2

##### helper functions #####
def read_name(prompt: str) -> str:
    while True:
        name = input(prompt).strip()
        if len(name) >= MINIMUM_NAME_LENGTH:
            return name
        print(f"Name must be at least {MINIMUM_NAME_LENGTH} characters long.")
        

def read_age(prompt : str) -> int:
       while True:
        try:
            age = int(input(prompt).strip())
            if age in range(MINIMUM_AGE, MAXIMUM_AGE + 1):
                return age
            print(f"Age must be between {MINIMUM_AGE} and {MAXIMUM_AGE}.")
        except ValueError:
            print("Please enter a whole number.")

def read_email(prompt: str) -> str:
    while True:
        email = input(prompt).strip()
        if "@" in email and "." in email:
            return email
        print("Invalid email format.")

def read_salary(prompt: str) -> float:
    while True:
        try:
            salary = float(input(prompt).strip())
            if salary >= 0:
                return salary
            print("Salary must be a greater than zero.")
        except ValueError:
            print("Please enter a valid number.")

def display_registration(name: str, age: int, email: str, salary: float) -> None:
    print(f"Registration Complete")
    print(f"Employee Name: {name}")
    print(f"Age: {age}")
    print(f"Email: {email}")
    print(f"Salary: ${salary:.2f}")

def main() -> None:
    print("Employee Registration")
    name = read_name("Enter Employee Name: ")
    age = read_age("Enter age: ")
    email = read_email("Enter email: ")
    salary = read_salary("Enter annual salary: ")
    display_registration(name, age, email, salary)

if __name__ == "__main__":
    main()

