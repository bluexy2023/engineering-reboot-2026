#!/usr/bin/env bash

my_var="Hello World"

# print variable value
echo "$my_var"

#concatenating this with another string
echo "${my_var}ly!"

#numerical variables
first_num=5
second_num=8

# arithmetic operation using $(())
echo "Sum: $(( first_num + second_num ))"