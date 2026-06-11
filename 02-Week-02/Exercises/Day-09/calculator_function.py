# calculator function program
# this program will perform basic mathematical operation
# it takes 2 parameters and dreturns the value of the operation

def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
sum = add_numbers(number1, number2)
print(str(number1) + " + " + str(number2) + " = " + str(sum))

