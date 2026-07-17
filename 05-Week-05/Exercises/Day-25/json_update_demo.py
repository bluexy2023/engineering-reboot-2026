# json update demo.py
# Exercise 3 of Day 25

# Requirement:
# Increase employee ID 1005 salary by 5%, save the file, 
# and verify persistence.
import json

def load_employees() -> list:
    with open("employees.json","r") as file:
        return json.load(file)
    

def save_employees(employees : list) -> None:
    with open("employees.json", "w") as file:
        json.dump(employees,file)


employees = load_employees()

# let's increase employee ID 1005's salary by 5%
# let's find that employee
# we are using a generator object to get the exact match
# by the use of the '()' operator, next means it returns as soon
# as it gets a match and not iterate any further.

employee_1005 = next((emp for emp in employees if emp['id'] == 1005), None)
if employee_1005:
    # let's increase it's salary by 5%
    employee_1005['salary'] += employee_1005['salary'] * 0.05

# now let's save our update
save_employees(employees)



