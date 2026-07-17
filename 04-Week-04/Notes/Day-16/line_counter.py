# line_counter.ph
# Exercise 1 of Day 17

# Open an existing file
# Read all records in the file
# Count the number of lines
# Display the total line count
# Program exits cleanly

line_count=0
with open("text_file.txt", "r") as file:
    for line in file:
        # iterate through all lines
        line_count += 1 # increment line count
print("Total lines:", line_count)