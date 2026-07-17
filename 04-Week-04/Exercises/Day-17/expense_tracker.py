# Expense tracker program
# Exercise 3 of Day 17

# Functional Requirements
# • Load expense records from a text file
# • Process all stored expense entries
# • Calculate total expenses
# • Display a summary report
# • Exit cleanly after processing

expenses_total=0
with open("expenses.txt", "r") as file:
    print("Here's the itemized expenses:")
    print("============================+")
    for line in file:
        line= line.strip()
        print("-", line)
        expenses_total += float(line)
    print("Our total expenses:", expenses_total)

