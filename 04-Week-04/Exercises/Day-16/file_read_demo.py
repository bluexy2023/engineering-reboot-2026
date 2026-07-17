# file_read_demo python program
# Exercise 2 for Day 16

# read and display content from a text file

with open("file_write_demo.txt", "r") as file:
    contents=file.read()
    if contents !=  "":
        print(contents)
    else:
        print("File empty")