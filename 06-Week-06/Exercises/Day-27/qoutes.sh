#!/usr/bin/env bash

# understanding quouting behavior

# weak quouting
# expands variables within it
# preserves spaces
var="Hello World"

echo "$var"

echo $var

# strong/tight quouoting, now variable expansion
# inside
echo '$var'

var2='Hello City'

echo $var2

my_file="my project.txt"

#rm $my_file  # this expands to 'rm my project.xt', which would 
             # try to delete files; "my" and "project.xt"

# do this instead
rm "$my_file"

# globbing (wildcard expansion)

my_search="*.txt"


echo $my_search  # searches local dir for files *.txt

echo "$my_search" # echoes literal *.txt 

## Rule of thumb ##
# Always quoute variables, lest they'd be expanded (glob)
# or if they have spaces in between, be considered as multiple
# paramenters when sent to a command


#Want literal text? Use single quotes '...'.

#Referencing a variable? Use double quotes "$var".

#Passing variables to commands (paths, names)? 
# Always wrap them in double quotes "$my_file".