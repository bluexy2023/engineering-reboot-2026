# number list python program 
# a Day 12 python exercise

# create an array or list of numbers

numbers = [10,20,30,40,50]

# use a for loop to 
# -- Display each number
# -- calculate a running total, then display at the end

# initialize total variable
total=0

# iterate through each number in the list
for number in numbers:
    # calculate running total
    total += number
    print(number)
print("Total:", total)