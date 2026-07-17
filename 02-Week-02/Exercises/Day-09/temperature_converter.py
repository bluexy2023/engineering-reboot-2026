# temperature converter program
# the program takes a temeprature in Celsius
# and returns the equivalent temperature in Fahrenheit

def celcius_to_fahrenheit(celcius):
    fahrenheit = 32 + (celcius * 9 / 5)
    return fahrenheit

# get user input
celcius = float(input("Enter temperature in Celcius: "))
# convert to Fahrenheit
fahrenheit = celcius_to_fahrenheit(celcius)
# display the result

print(str(celcius) + " degrees Celcius is equal to " + str(fahrenheit) + " degrees Fahrenheit.")
