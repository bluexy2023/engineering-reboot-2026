# sort demo program
# exercise 3 of Day 24

from employee_data import EMPLOYEES as employees
"""
Tasks
• Sort by name.
• Sort by salary (ascending and descending).
• Sort by age.
• Perform multi-level sorting by department then name.
• Display the top three highest-paid employees
"""

def sort_by_name(employees: list) -> list:
    return sorted(employees, key = lambda employee: employee['name'])

def sort_by_salary_asc(employees: list) -> list:
    return sorted(employees, key = lambda employee: employee['salary'])

def sort_by_salary_desc(employees: list) -> list:
    return sorted(employees, key = lambda employee: employee['salary'], reverse=True)

def sort_by_age(employees: list) -> list:
    return sorted(employees, key=lambda employee: employee['age'])

def sort_by_dept_and_name(employees: list) -> list:
    return sorted(employees, key= lambda x: (x['department'],x['name']))

def top_3_earners(employees: list) -> list:
    return sorted(employees, key = lambda emp: emp['salary'], reverse=True)[:3]

print("Sorted by name")
print("--------------")
sorted_by_name = sort_by_name(employees)
for emp in sorted_by_name:
    print(emp)

print("\nSorted by salary ascending")
print("--------------------------")
for emp in sort_by_salary_asc(employees):
    print(emp)

print("\nSorted by salary descending")
print("---------------------------")
for emp in sort_by_salary_desc(employees):
    print(emp)

print("\nSorted by age")
print("---------------")
for emp in sort_by_age(employees):
    print(emp)

print("\nSorted by department and name")
print("-------------------------------")
for emp in sort_by_dept_and_name(employees):
    print(emp)

print("\nTop 3 earners")
print("---------------")
for emp in top_3_earners(employees):
    print(emp)