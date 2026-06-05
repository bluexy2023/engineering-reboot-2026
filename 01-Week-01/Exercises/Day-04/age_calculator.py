# age calculator exercise

# ask the user for their name and the year they were born
# then compute their age and print it out 

name = input("What is your name? ")

year_born = input("What year were you born? ")

age = 2026 - int(year_born)

print("Hello " + name + ", you are " + str(age) + " years old.")

# observations:
# -- the input() function takes in user input as a string
# -- the int() function converts a string to an integer
# -- the str() function converts an integer to a string
# -- the print() function can take in variables of different types

