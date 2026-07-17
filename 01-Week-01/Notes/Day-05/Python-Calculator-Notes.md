Markdown

# what input() does

-- input halts execution of a program until an text is typed in a prompt or terminal.  whatever is typed in the terminal will be assigned to the variable 

# variable assignment
-- is the process of assigning the value of the text typed in from the input() command

# float()
- float converts the text input into a decimal value
- ex.  2 becomes 2.0

# arithmetic operators '+', '-' , '*', '/' are addition, subtraction, multiplication and division respectively, and they only apply to numeric numbers like integers, float and other numeric types. the '+' can act as a concatenation operator for strings

# program flow is the sequence of execution the program performs -- for python, it is from top to bottom, line per line, unless redicted to jump to a different area of the code

## sample calculator program ... copied

# Engineering Reboot 2026
# Week 01 Day 05
# Calculator Project

## print a welcome message to the user
## telling it what this program is trying to do
print("calculator.py implemntation for Engineering Reboot 2026")

# as for first number

first_num = input ("enter the first number:")
second_num = input ("enter the second number:")

# convert the input to a float
first_num = float(first_num)
second_num = float(second_num)

# now Calculate

## Addition
sum = first_num + second_num

## Subtraction
diff = first_num - second_num

## Multiplication
prod = first_num * second_num

## Division
quot = first_num / second_num


## display the results

print ("Addition: " + str(sum))
print ("Subtraction: " + str(diff))
print ("Multiplication: " + str(prod))
print ("Division: " + str(quot))






