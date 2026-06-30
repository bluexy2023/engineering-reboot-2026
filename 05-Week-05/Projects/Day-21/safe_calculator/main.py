# our main calculator code

from calculator import add, subtract, multiply, divide
from input_helpers import read_float, read_menu_choice

# display_menu function
def display_menu() -> None:
    print("Safe Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
def run_calculation(choice: str) -> None:
    first = read_float("Enter first number: ")
    second = read_float("Enter second number: ")
    try:
        if choice == "1":
            result = add(first, second)
        elif choice == "2":
            result = subtract(first, second)
        elif choice == "3":
            result = multiply(first, second)
        elif choice == "4":
            result = divide(first, second)
        # let's catch the wrong selection 
        # outside of this function 
        #else:
        #    print("Invalid menu selection.") 
        #    return
    except ZeroDivisionError as error:
        print(f"Calculation error: {error}") 
    else: print(f"Result: {result}")

VALID_CHOICES = {"1","2","3","4"}    
def main() -> None:
    while True:
        display_menu()
        choice = read_menu_choice()
        if choice == "5":
            print("Exiting Safe Calculator.")
            break
        if choice in VALID_CHOICES:
            run_calculation(choice)
        else:
            print("Invalid menu selection.")
        
if __name__ == "__main__":
    main()