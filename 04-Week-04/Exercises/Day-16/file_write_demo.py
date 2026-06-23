# file_write_demo python program
# Day 16, Exercise 1
# open a file for writing, write to file user
# specified text (input)

# for the purpose of this exercise, let's hardcode
# the filename

output_file="file_write_demo.txt"

# prompt for user input

input_text=input("Enter text for storing:")

# open file for writing, use "w" as parameter to open
# use 'with' statement

with open(output_file, "w") as file:
    file.write(input_text)
    print("File write successful.")
