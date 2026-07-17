# validate numeric input

# function to prompt for numeric input
def read_number(prompt : str) -> float:
    while True:
        try:
             return (float(input(prompt).strip()))
        except ValueError:
            print("Invalid input. Try again.")
        

value = read_number("Enter your salary:")
print(f"value: {value}")