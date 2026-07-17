# sum calculator program
# use an accumulator variable and for loop and  range() to get a total
# value of 5050

total = 0 # initialize accumulator variable

for number in range(1, 101):
    total += number  # or total = total + number

print(total)