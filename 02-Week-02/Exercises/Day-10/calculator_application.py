
# this is the day 10 project of week 2 of engineering
# bootcamp 2026
# expected to use (while or for) loops and functions to be create 
# a calculator application that incorporates a menu and
# allows the user to perform basic arithmetic operations

## Function to display the menu
def display_menu():
    print("===== CALCULATOR =====")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Exit")

## Function to perform addition
def add_numbers(num1, num2):
    return num1 + num2

## Function to perform subtraction
def subtract_numbers(num1, num2):
    return num1 - num2

## Funtion to perform multiplication
def multiply_numbers(num1, num2):
    return num1 * num2

## FUnction to perform division
def divide_numbers(num1, num2):
    if (num2 !=0):
        return num1 / num2
    else:
        print ("Cannot divide by zero.")
        return None 
        ## by default, None is returned if no explicit return is provided


## main program
result = None
while True:
    display_menu()
    operation = int(input("Select an operation (1-5): "))
    if (operation == 5):
        ## debugging purposes:
        print("Exit. ")
        break
    elif operation in [1, 2, 3, 4]:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        if operation == 1:
            result = int(add_numbers(num1, num2))
        elif operation == 2:
            result = int(subtract_numbers(num1, num2))
        elif operation == 3:
            result = int(multiply_numbers(num1, num2))
        elif operation == 4:
            result = divide_numbers(num1, num2)
    else: # invalid selection. Nothing is stated in the requirements
          # we'll just go back to the menu
          continue  # this will skip the rest of the loop and go back
    
    if result is not None: # means, a successful operation was performed
        print("Result: " + str(result))