# json read demo program
# exercise 2 for day 25
import json

def display_employee_data(employees: list) -> None:
    for employee in employees:
        print(employee)

with open("employees.json", "r") as file:
    employee_data = json.load(file)
    if employee_data:
        display_employee_data(employee_data)

