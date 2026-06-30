# input helpers module

# this function will keep on asking for input
# until a valid floating point is provided
# when it does, it returns the float value to the caller
# this uses the input() function to request for user input
# casts it to float, and catches exception caused by the casting
# method
def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError: 
            print("Invalid numeric input. Please enter a valid number.")

# this function just returns the string for the option chosen
# by the user based on the menu display
# strip() removes leading and trailing spaces
def read_menu_choice() -> str: 
    return input("Choose an option: ").strip()