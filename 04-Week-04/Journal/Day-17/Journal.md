# Day 17 Journal

# Summary
- learned about file processing today by reading lines in a file and counting words within it.
- also learned about reading values from a file by the use of iteration within a file, an performing calculations within it.
# Challenges Encountered
- at first I was surprised that I could not anymore read lines from a file after I dumped its contents through a read() on a file descriptor
# Solutions Applied
- instead of performing a read() prior to dumping the contents of the file, i did a for loop on a file descriptor to give me access to each line.  Only then did I decide to dump it line by line as part of the summary of expenses, and then compute a running total of the expenses to be displayed when the loop ends.
# Confidence Assessment
9/10
# Reflection
- python has an easy approach to text file processing. 
# Tomorrow Preparation
- generate day 18 field manual with chatgpt, and perform some quick code samples for the upcoming day's activity