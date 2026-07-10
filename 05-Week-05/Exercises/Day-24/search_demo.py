# search demo program
# exercise 1 for Day 24

#########  Tasks #############
# Create find_employee_by_id(employee_id) that returns the 
#   matching employee dictionary orNone.
# Create find_employee_by_name(name) that performs 
#  case-insensitive partial matching.
# Display a friendly message when no employee is found.

from employee_data import EMPLOYEES as employees
import sys  # for command line arguuments for testing


## function to iterate through the employee list and find 
## a record that matches the employee_id. If found, return the 
## employee dictionary, otherwise return None.
def find_employee_by_id(employee_id: int) -> dict:
    for employee in employees:
        if employee['id'] == employee_id:
            return employee
    return None

"""
Function to iterate through the employee list and search for the record
for which the name partially matches the input name.  By partial match, 
we mean that the input name can be a substring of the employee's name.
To make it non-case-sensitive, we will convert both the input name and the employee's 
name t lowercase before doing the comparison.  If a match is found, we will
append it to our local list of matching employees.  If no match is found, we will return 
an empty list
"""
def find_employee_by_name(name: str) -> list:
    matching_employees = []
    for employee in employees:
        if name.lower() in employee['name'].lower():
            matching_employees.append(employee)
    

    return matching_employees

def main(arg1: int, arg2: str)  -> None:
    # test find employee by id
    print("Testing find_employee_by_id with employee_id:", arg1)
    print("-----------------------------------------------")
    employee = find_employee_by_id(arg1)
    if employee:
        print("Employee found:", employee)
    else:
        print("No employee found with ID:", arg1)

    # test find employee by name
    print("\nTesting find_employee_by_name with name:", arg2)
    print("-----------------------------------------------")
    matching_employees = find_employee_by_name(arg2)
    if matching_employees:
        print("Matching employees found.")
        for emp in matching_employees:
            print(emp)
    else:
        print("No employees found matching with name:", arg2)

if __name__ == "__main__":
    if len(sys.argv) != 3:  # should pass 2 parameters, arg0 is the script name
        print("Usage: python search_demo.py <employee_id> <name>")
        sys.exit(1) 
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: employee_id must be an integer.")
        sys.exit(1)
        
    name = sys.argv[2]
    main(employee_id, name)