"""Mini Project
Persistent Employee Directory supporting load, 
display, search, add, update, delete, save and exit."""
# a mini project for day 25 for persistent data
import json

data_file = "employees.json"

def read_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).strip())
            if value > 0:
                return value
            print("Value must be a greater than zero.")
        except ValueError:
            print("Please enter a valid number.")

def read_positive_integer(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
            print ("Value must be greater than zero.")
        except ValueError:
            print("Must enter a whole number.")

def read_string(prompt: str) -> str:
    while True:
        string = input(prompt).strip()
        if string:
            return string
        print("Input cannot be empty.")

def load_employees(data_file: str) -> list:
    with open(data_file,"r") as file:
        return json.load(file)
    
def save_employees(employees: list, data_file: str) -> None:
    with open(data_file,"w") as file:
        json.dump(employees, file, indent=4)

## search by ID
def search_employee(employees, employee_id) ->dict:
    return next((emp for emp in employees if emp['id'] == employee_id),None)


def add_employee(employees, employee_record) -> None:
    # let's prevent duplicated employee IDs
    if search_employee(employees, employee_record['id']) == None:
        employees.append(employee_record)
    else:
        print(f"Employee with ID: {employee_record['id']} already exists!")
        print("Add Employee failed!")

def delete_employee(employees: list, employee: dict) -> None:
    employees.remove(employee)
    
    
def display_employees(emps : list) -> None:
    print(f"\n{'ID':<6}{'Name':<20}{'Department':<18}{'Age':>5}{'Salary':>12}")
    print("-" * 59)
    for emp in emps:
        print(f"{emp['id']:<6}"
              f"{emp['name']:<20}"
              f"{emp['department']:<18}"
              f"{emp['age']:>5}"
              f"{float(emp['salary']):>12}"
              )
        
def create_employee_from_input() -> dict:
    new_employee = {}
    # let's create the employee record
    new_employee['id'] = read_positive_integer("Enter Employee ID: ")
    new_employee['name'] = read_string("Enter Employee Name: ")
    new_employee['department'] = read_string("Enter Employee Department: ")
    new_employee['age'] = read_positive_integer("Enter Employee Age: ")
    new_employee['salary'] = read_positive_float("Enter Employee Salary: ")
    return new_employee


# update_employee, let's focus on hard-coding changing those fields that
# are obviously going to change
# let's keep the name unchanged for now.  ID technically doesn't change
# Future enhancement:
# - Support partial updates.
# - Protect immutable fields generically.
# - Validate business rules.
# - Audit changes.
def update_employee(employee: dict) ->None:
    employee['department'] = read_string("Enter Employee Department: ")
    employee['age'] = read_positive_integer("Enter Employee Age: ")
    employee['salary'] = read_positive_float("Enter Employee Salary: ")
    
        

def display_menu():
    print("\nPersistent Employee Directory")
    print("==============================")
    print("1. Display Employees")
    print("2. Search Employee")
    print("3. Add Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Save Employees")
    print("7. Exit")
    
def main() -> None:
        employees = load_employees(data_file)
        while True:
            display_menu()
            menu_choice = read_string("Enter Selection: ")
            if menu_choice == "1":
                display_employees(employees)
            elif menu_choice == "2":
                employee_id = read_positive_integer("Enter Employee ID: ")
                employee = search_employee(employees, employee_id)
                if employee is not None:
                    display_employees([employee])
                else:
                    print(f"Employee with Employee ID: {employee_id} not found")
            elif menu_choice == "3":
                employee = create_employee_from_input()
                add_employee(employees, employee)
            elif menu_choice == "4":
                employee_id = read_positive_integer("Enter ID of Employee to Update: ")
                employee_to_update = search_employee(employees,employee_id)
                if employee_to_update is not None:
                    update_employee(employee_to_update)
                else:
                    print(f"Employee with Employee ID: {employee_id} not found")
            elif menu_choice == "5":
                employee_id = read_positive_integer("Enter ID of Employee to Delete: ")
                employee_to_delete = search_employee(employees,employee_id)
                if employee_to_delete is not None:
                    delete_employee(employees,employee_to_delete)
                else:
                    print(f"Employee with Employee ID: {employee_id} not found")
                
            elif menu_choice == "6":
                save_employees(employees,data_file)
            elif menu_choice == "7":
                # check if there were changes to the data before exiting, and offer
                # option to save or not
                # This is where we need to load the data again and compare its contents
                # with the in-memory employee data
                if employees == load_employees(data_file):
                    print("No changes in the data... exiting ...")
                    break
                # else we have modified the employee data, employees
                else:
                    print("Employee Data Changed!")
                    while True:
                        choice=input("Save before exit? Yes/No: ").strip().lower()
                        if choice == "yes":
                            save_employees(employees,data_file)
                            print("Changes saved .. exiting ...")
                            break
                        elif choice == "no":
                            print("Exiting without saving...")
                            break
                        else:
                            continue
                    break                          
            else:
                print("Invalid Menu Choice!")


if __name__ == "__main__":
    main()
    










