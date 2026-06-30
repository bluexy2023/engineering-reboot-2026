</Markdown>

# Day 21 Notes

# Concepts Learned
- learned about exception handling and creating very clean 
  and robust program that handles invalid inputs
- also learned to raise own exception with custom error messages that is specific to the case being caught

# Key Commands
try, except, else in conjunction with try to perform an alternative path where no exception occured, finally, to perform a block in the try group to execute code under that block whether an exception occured or not.

# Key Observations
- function definitions can define an input parameter (for readability, and also to indicate that the caller has already validated all inputs), ex. def func(var : int) -> float, func takes on an int and returns a float
- using a try, except block help programs to handle invalid inputs, without crashing the program

# Lessons Learned
- learned the difference between syntax errors and runtime errors
- through today's exercises, I was able to understand the concept of exceptions and handling them for a graceful performance or exit of programs
- also, modules where incorporated into the program which built upon the lessons learnt from the previous sessions.

# Questions For Future Study
- how to do you handle exceptions for which you don't know the type ? 
Answer: do this
except Exception as error:
    print(type(error).__name__)
    print(error)
-- with the above debug line, you'd know which Exception type you are going to catch in your code. :)

