</Markdown>

# Day 17 Notes

# Concepts Learned
- reading a file for analysis line by line
- reading values from a file
- calculating number of lines and number of words in a file
- aggregating from a collection of words read from a file
# Key Commands
with, open, and as keywords, for, print, len, strip(), += operator
# Key Observations
- files can be read line by line by the treating it as a stream, a file that has already been read cannot be iterated as a stream anymore
# Lessons Learned
- when iterating lines in a file, don't perform a read() of the file descriptor, as it is going to be consumed, and could not anymore be read
# Questions For Future Study
- how to re-read a file that has been read within the same program ?
