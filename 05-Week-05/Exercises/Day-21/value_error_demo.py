# Exercise 1 of Day 21
# Convert user input to a number and 
# recover when the input is not numeric.

while True:
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        print(f"Accepted Value:{number}")
        break
    except ValueError:
        print("Invalid numeric input. Please try again.")

