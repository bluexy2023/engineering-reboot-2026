# data manipulation program
# exercise 1 for day 23
from employee_data import EMPLOYEES as employees

#Display every employee.
#Display the total number of employees.
#Access the first employee.
#Access the last employee.
#Add a new employee to the end of the list (append()).
#Insert a new employee at a specified position (insert()).
#Remove an employee by index (pop()).
#Remove an employee by value (remove()), if appropriate.
#Iterate through the list using a for loop.
#Verify the final employee count.

def display_every_employee(employees):
    for employee in employees:
        print(employee)
def display_total_employees(employees):
    print(f"Total Employees:{len(employees)}")
def access_first_employee(employees):
    first_employee = employees[0]
    print(f"First Employee: {first_employee}")
def access_last_employee(employees):
    last_employee = employees[-1]
    print(f"Last Employee: {last_employee}")
def add_new_employee(employees, new_employee):
    print(f"Adding New Employee: {new_employee}")
    employees.append(new_employee)
    print(f"New Employee Data Becomes: {employees}")

def insert_new_employee_at_position(employees,new_employee,position):
    print(f"Inserting New Employee:{new_employee} at position: {position}")
    employees.insert(position,new_employee)
    print(f"New Employee Data Becomes: {employees}")

def remove_employees_n(employees,index):
    employees.pop(index)
    print(f"Removed Employee at index: {index}")
    print(f"New Employee Data Becomes: {employees}")

def remove_employee_by_value(employees,employee):
    print(f"Removing Employee: {employee}")
    employees.remove(employee)
    print(f"New Employee Data Becomes: {employees}")

if (__name__ == "__main__"):
    display_every_employee(employees)
    display_total_employees(employees)
    access_first_employee(employees)
    access_last_employee(employees)
    add_new_employee(employees,{"id":1006,"name":"Glenn","age":53,"department":"Finance","salary":100000})
    insert_new_employee_at_position(employees,
                                    {"id":1008,"name":"Thotho","age":45,"department":"Marketng","salary":120000},3)
    remove_employees_n(employees,2)
    employee_to_remove = employees[1]
    remove_employee_by_value(employees,employee_to_remove)
    display_every_employee(employees)
    display_total_employees(employees)