# temperature converter exercise
# ask the user for a temperature in Celcius and convert it to Fahrenheit

temp_celcius = input("Input temperature in Celcius: ")

temp_fahr = float(32 + int(temp_celcius) * 9 / 5)

print(str(temp_celcius) + " degrees Celcius in Fahrenheit is: " + str(temp_fahr) )

# Observations:
# the introduction of the float() function allows us to convert the result of the computation to a decimal number 
# since a division operation can result in a non-whole number.
# everytime we concatenate a string with a variable, we need to convert it to a string using the string() function
# the '+' symbol within the print() function is used to concatenate strings on the same line. 
# it is not a mathematical operator in this context.