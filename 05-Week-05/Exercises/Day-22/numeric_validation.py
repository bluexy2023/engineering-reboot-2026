# validate numeric input

# function to prompt for numeric input
def read_number(prompt : str) -> float:
    while True:
        try:
             return (float(input(prompt).strip()))
        except ValueError:
            print("Invalid numeric input. Please try again.")
        

value = read_number("Enter Amount:")
print(f"Accepted Value: {value}")