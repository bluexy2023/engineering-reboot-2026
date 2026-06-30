# exercise 5 of day 21
# use of finally 
# Demonstrate logic that runs regardless of 
# success or failure.

try: 
    filename = input("Enter filename to open: ") 
    file = open(filename, "r") 
    print(file.read())
except FileNotFoundError: 
    print("File was not found.")
finally: 
    print("File operation attempt completed.")