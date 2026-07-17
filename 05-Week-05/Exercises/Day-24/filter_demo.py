# filter demo program
# exercise 2 for Day 24

'''Objective
Create subsets of employee records without modifying the original dataset.
Program: filter_demo.py
Tasks
• Display Engineering employees.
• Display employees earning more than $80,000.
• Display employees older than 35.
• Combine multiple filtering criteria.

Challenge: A reusable filtering function that accepts a predicate'''


from employee_data import EMPLOYEES as employees
import sys  # for command line arguuments for testing

def filter_engineering_employees() -> list:
    # let's use a list comprehension to filter the employees
    return [employee for employee in employees if employee['department'] == 'Engineering']

def filter_employees_over_80k() -> list:
    # let's use a list comprehension to filter the employees
    return [emp for emp in employees if emp['salary'] > 80000]

def filter_employees_above_35() -> list:
    # continue to practice list comprehension 
    return [emp for emp in employees if emp['age'] > 35]

def filter_engineering_above_35() -> list:
    # combine multiple filtering criteria using list comprehension
    return [ emp for emp in employees if emp['department'] == 'Engineering' and emp['age'] > 35]

# our reusable filtering function which uses a callable
def filter_items(items : list,predicate: callable) -> list:
    return [item for item in items if predicate(item)]


def main() -> None:
    print("Engineering students:")
    for emp in filter_engineering_employees():
        print(emp)
    
    print("\nEmployees earning more than 80k")
    for emp in filter_employees_over_80k():
        print (emp)
    
    print("\nEmployees above 35")
    for emp in filter_employees_above_35():
        print(emp)

    print("\nEngineering Employees above 35")
    for emp in filter_engineering_above_35():
        print(emp)

    print("\nNow using our reusable filtering function")
    print("Let's filter all employees whose age are odd number")
    even_aged_employees = filter_items(employees, lambda employee: employee['age'] % 2 == 1)
    for emp in even_aged_employees:
        print(emp)


if __name__ == "__main__":
    main()
