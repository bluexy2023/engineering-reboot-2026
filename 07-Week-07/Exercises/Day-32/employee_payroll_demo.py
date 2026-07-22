# employee_payroll_demo.py
# exercise 4 of Day 32
from employee_methods import Employee

emp1 = Employee(10001,"Aida", "Marketing", 95000)
emp2 = Employee(10002,"Lorna", "Finance", 93000)
emp3 = Employee(10003,"Fe", "Engineering", 105000)
emp4 = Employee(10004,"Imelda", "HR", 86000)

employees = [emp1,emp2,emp3,emp4]

print("Current State of Employees")
print("--------------------------")
for employee in employees:
    employee.display_information()
# loop through the employees and perform targeted department
# transfer and targeted raises
# Rule: if employee is in Finance, raise salary by 10%
#       transfer to Marketing if salary is less than 90000
for employee in employees:
    if employee.get_annual_salary() < 90000:
        employee.transfer_department("Marketing")
    if employee.department == "Finance":
        employee.apply_raise(10)

print("\nNew State of Employees")
print("----------------------")
for employee in employees:
    employee.display_information()
