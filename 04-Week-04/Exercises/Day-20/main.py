# main python code for exercise 3 for Day 20
from calculator_module import *

def display_menu():
    print("=========================")
    print("ENGINEERING CALCULATOR")
    print("=========================")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

selection=None
while True:
    display_menu()
    try:
        selection = int(input("Input Selection: "))
    except ValueError:
        print("Only accepts integer!")
        continue
    if selection == 1:
        num1 = float(input("Input first number:"))
        num2 = float(input("Input second number:"))
        print ("Addition:",add(num1,num2))
    elif selection == 2:
        num1 = float(input("Input first number:"))
        num2 = float(input("Input second number:"))
        print ("Subtraction:",subtract(num1,num2))
    elif selection == 3:
        num1 = float(input("Input first number:"))
        num2 = float(input("Input second number:"))
        print ("Multiplication:",multiply(num1,num2))
    elif selection == 4:
        num1 = float(input("Input first number:"))
        num2 = float(input("Input second number:"))
        try:
            quotient = divide(num1,num2)
            print ("Division:",quotient)
        except ValueError as e:
            print(e)
            continue
    elif selection == 5:
        break
    else:
        print("Operation not in menu!")

# let's call our power, modulus and floor_division functions
sample_values = [(5,3),(7,2),(4,0)]
for test_case in sample_values:
    print("Test Case:", test_case)
    try:
        result = power(*test_case)
        print("Power:", result)
        result = modulus(*test_case)
        print("Modulus:", result)
        result = floor_division(*test_case)
        print("Floor division:", result)
    except ValueError as error:
        print(error)