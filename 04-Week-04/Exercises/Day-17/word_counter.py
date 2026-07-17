# word_counter python program
# Exercise 2 of Day 17

#Objective: Count the number of words contained within a text file.
#Requirements
#• Open an existing text file
#• Read file contents
#• Count words contained within the file
#• Display total word count
#• Program exits cleanly

num_words = 0
with open("text_file.txt", "r") as file:
    for line in file:
        words = line.split()
        num_words += len(words)
print("Total number of words:", num_words)