# employee reporting system
# mini-project for day 24

"""
Mini Project — Employee Reporting System
Build a menu-driven reporting system supporting search by ID, 
search by name, Engineering employee report, high salary report,
age report, department summary, payroll summary,highest-paid employee, 
lowest-paid employee, and average salary. 

Each menu option should call a dedicated reusable function.
"""

from employee_data import EMPLOYEES as employees

# our reusable filter function
def filter_items(items : list, predicate: callable) ->list:
    return [item for item in items if predicate(item)]

# our reusable sorting function
def sort_items(items: list, key_function: callable, ascending: bool = True) ->list:
    return sorted(items, key=key_function, reverse= not ascending)

# displaying employee details with formatting
def display_employee_details(emps: list) -> None:
    print(f"\n{'ID':<6}{'Name':<20}{'Department':<18}{'Age':>5}{'Salary':>10}")
    print("-" * 59)
    for emp in emps:
        print(f"{emp['id']:<6}"
              f"{emp['name']:<20}"
              f"{emp['department']:<18}"
              f"{emp['age']:>5}"
              f"{emp['salary']:>10}"
              )
        
## search by ID
def search_by_id() -> None:
    print("\nSearch by ID")
    print("------------")
    while True:
        try:
            ID = int(input("Enter ID: "))
            employee_match = filter_items(employees, lambda item: item['id'] == ID)
            if employee_match:
                display_employee_details(employee_match)
            else:
                print(f"Employee with ID {ID} not found.")
            break
        except ValueError:
            print("ID must be a whole number. Try again")
            continue

## search by name
def search_by_name() -> None:
    print("\nSearch by Name")
    print("--------------")
    while True:
        name = input("Enter Employee Name: ").strip()
        if name:
            employee_match = filter_items(employees, lambda item: name.lower() in item['name'].lower())
            if employee_match:
                display_employee_details(employee_match)
            else:
                print(f"Employee with name {name} not found.")
            break
        else:
            print("Name cannot be empty. Try again")
            continue

## engineering employee report
def engineering_employee_report() ->None:
    print("\nEngineering Employees Report")
    print("----------------------------")
    engineering_employees = filter_items(employees, lambda employee: employee['department'] == "Engineering")
    if engineering_employees:
        display_employee_details(engineering_employees)

## high salary report
## only filter those whose salaries are above 90000
def high_salary_report() -> None:
    print("\nHigh Salary Report")
    print("------------------")
    high_salary_employees = filter_items(employees, lambda emp: emp['salary' ]> 90000)
    if high_salary_employees:
        display_employee_details(high_salary_employees)

# Age Report
def age_report() -> None:
    print("\nAge Report")
    print("----------")
    sorted_by_age = sort_items(employees, lambda emp: emp['age'], ascending = True)
    if sorted_by_age:
        display_employee_details(sorted_by_age)

# department summary 
def department_summary() -> None:
    print("\nDepartment Summary")
    print("------------------")
    departments = {}
    for employee in employees:
        department = employee['department']
        if department in departments:
            departments[department] += 1
        else:
            departments[department] = 1
    for departmentname, number_employees in departments.items():
        print(f"{departmentname:<16}{number_employees} employees")

# payroll summary 
def payroll_summary():
    print("\nPayroll Summary")
    print("---------------")
    # employee count
    employee_count = len(employees)
    total_payroll = sum(emp['salary'] for emp in employees)
    average_salary = total_payroll / employee_count
    lowest_salary = min(emp['salary'] for emp in employees)
    highest_salary = max(emp['salary'] for emp in employees)
    print("Employee Count:", employee_count)
    print("Total Payroll:", total_payroll)
    print("Average Salary:", average_salary)
    print("Lowest Salary:", lowest_salary)
    print("Highest Salary:", highest_salary)

# highest paid employee
def highest_paid_employee() -> None:
    print("\nHighest Paid Employee")
    print("---------------------")
    highest_earner = max(employees, key = lambda employee: employee['salary'])
    if highest_earner:
        display_employee_details([highest_earner])

# lowest paid employee
def lowest_paid_employee() -> None:
    print("\nLowest Paid Employee")
    print("--------------------")
    lowest_earner = min(employees, key=lambda employee: employee['salary'])
    if lowest_earner:
        display_employee_details([lowest_earner])


MENU = {
    "1" : {
        "description" : "Search by ID",
        "handler" : search_by_id
    },
    "2" : {
        "description" : "Search by Name",
        "handler" : search_by_name
    },
    "3" : {
        "description" : "Engineering Employee Report",
        "handler" : engineering_employee_report
    },
    "4" : {
        "description" : "High Salary Report",
        "handler" : high_salary_report
    },
    "5" : {
        "description" : "Age Report",
        "handler" : age_report
    },
    "6" : {
        "description" : "Department Summary",
        "handler" : department_summary
    },
    "7" : {
        "description" : "Payroll Summary",
        "handler" : payroll_summary
    },
    "8" : {
        "description" : "Highest Paid Employee",
        "handler" : highest_paid_employee
    },
    "9" : {
        "description" : "Lowest Paid Employee",
        "handler" : lowest_paid_employee
    },
    "10" : {
        "description" : "Exit"
    }
}



def display_menu()-> None:
    print("\nEmployee Reporting System")
    print("====================")
    for key in sorted(int(member) for member in MENU.keys()):
        print(f"{key:>2}.{MENU[str(key)].get("description")}")


def perform_operation(menu_choice):
    handler = MENU[menu_choice].get("handler")
    if handler:
        handler()

def main() -> None:
    while True:
        display_menu()
        choice = input("Enter selection: ")
        if choice == "10":
            print("Exiting. Bye.")
            break
        if choice in MENU:
            perform_operation(choice)
        else:
            print("Invalid selection! Try again.") 

if __name__ == "__main__":
    main()

