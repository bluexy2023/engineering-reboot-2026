</Markdown>

# Day 27 Notes

# Concepts Learned
Variable expansion
Command substitution
Quoting behavior
Pipes
Redirection
File permissions
Environment variables
Bash scripting practices
Differences between Bourne shell (sh) and Bash

# Key Commands
tee, df, uptime, echo, mkdir -p, $(shellcommand ), &&, ||, "", '', [[for strings]], (( for numbers))
for item in list

# Key Observations
Bash has shown its expressiveness in the many features it offers for command substition, variable expansion, command composition, among other things
## on quotations
"" quoutation style variables
'' treats variables literally
Use "" when you need to preserve spaces and expand
No quoutation on variables with contents with spaces would leak
   -  its spaces and will be treated as different parameters 
   -  when passed to commands
Use '' to treat values within the quoute as literal strings
## on file permissions 
chmod +x adds an executable flag to a file.  When we have this flag on, we can run directly the program by its filename, and it should be executed by the shell.  Without this, a "Permission Denied" error will be displayed

## on aliases
- Aliases improves productivity in that commands with very long
  parameters could be run by an alias, or using a shortened, and mnemonic name depending on the user.
  
   


# Lessons Learned
- created a reusable utility to gather system information

# Questions For Future Study
- continue to study linux for this week

