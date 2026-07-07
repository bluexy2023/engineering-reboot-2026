# dictionary manipulation
# exercise 3 for day 23
from employee_data import EMPLOYEES as employees

# locate employee by ID and display their information
# employee ID: 1002

employee_1002 = {}
for employee in employees:
    if employee["id"] == 1002:
        employee_1002 = employee
        break

print(f"Employee with ID 1002: {employee_1002}")

# update age and salary
employee_1002["age"] = 35
employee_1002["salary"] = 75000

print(f"Employee with ID 1002: {employee_1002}")

# add email key to the employee dictionary
employee_1002["email"] = "bob.smith@company.com"

print(f"Employee with ID 1002: {employee_1002}")

# remove the employee email key from the dictionary
del employee_1002["email"]

print(f"Employee with ID 1002: {employee_1002}")

# iterate through the employee dictioary and display key and value
for key,value in employee_1002.items():
    print(f"{key}: {value}")

# another approach
for key in employee_1002.keys():
    print(f"{key}: {employee_1002[key]}")