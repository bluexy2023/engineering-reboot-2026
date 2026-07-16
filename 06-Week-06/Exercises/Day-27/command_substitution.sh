#!/usr/bin/env bash

# command substitution exercise
# Exercise 2 of Day 27

# assign the std_out of command to variable through $(command)
result=$(date)

echo "Result: $result"

# check exit status of command
if found=$(ls glennj.txt 2> /dev/null ); then
    echo "File glennj.txt: $found"
else
    echo "File glennj.txt not found"
fi




