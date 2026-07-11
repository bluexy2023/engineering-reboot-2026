# json write demo program
# Exercise 1 for Day 25

# Write EMPLOYEES to 
# employees.json using json.dump(..., indent=4).

from employee_data import EMPLOYEES as employees
import json

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)