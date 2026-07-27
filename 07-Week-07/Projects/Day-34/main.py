from employee_directory import EmployeeDirectory
from employee_data import EMPLOYEES as employee_list


# helper methods here.  candidates for moving into its own module in the future
def read_id(prompt: str) -> int:
    while True:
        try:
            emp_id = int(input(prompt))
            if emp_id < 1:
                print("Employee ID must be a positive integer.")
            
            return emp_id
        except ValueError:
            print("Invalid input.")

def read_name(prompt: str) -> str:
    while True:
        name = input(prompt).strip()
        if name:
            return name
        else:
            print("Name cannot be empty.")

def print_menu() -> None:
    print("\nEmployee Directory Management System")
    print("1. Search Employee by ID")
    print("2. Search Employee by Name")
    print("3. Get Total Number of Employees")
    print("4. List Employees by Department")
    print("5. Get Average Salary")
    print("6. Get Highest Salary Employee")
    print("7. Sort Employees by Salary")
    print("8. Sort Employees by Name")
    print("9. Exit")

def main() -> None:
    # instantiating our EmployeeDirectory class
    employee_directory = EmployeeDirectory()
    # let's load data from employee_list
    employee_directory.load_data(employee_list)
    while True:
        print_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            emp_id = read_id("Enter Employee ID: ")
            employee = employee_directory.search_by_id(emp_id)
            if employee is not None:
                employee.display()
            else:
                print("Employee not found.")

        elif choice == "2":
            name = read_name("Enter Employee Name: ")
            employee = employee_directory.search_by_name(name)
            if employee is not None:
                employee.display()
            else:
                print("Employee not found.")

        elif choice == "3":
            count = employee_directory.get_count()
            print(f"Total number of employees: {count}")

        elif choice == "4":
            department = read_name("Enter Department Name: ")
            dept_employees = employee_directory.get_by_department(department)
            if dept_employees:
                for emp in dept_employees:
                    emp.display()
                    print("-" * 20)
            else:
                print("No employees found in this department.")

        elif choice == "5":
            avg_salary = employee_directory.get_average_salary()
            print(f"Average salary: ${avg_salary:.2f}")

        elif choice == "6":
            highest_paid_employee = employee_directory.get_highest_paid()
            if highest_paid_employee is not None:
                highest_paid_employee.display()
            else:
                print("No employees found.")

        elif choice == "7":
            sorted_by_salary_employees  = employee_directory.sort_by_salary()
            if sorted_by_salary_employees is not None:
                for employee in sorted_by_salary_employees:
                    employee.display()
            else:
                print("No employees found.")

        elif choice == "8":
            sorted_by_name_employees = employee_directory.sort_by_name()
            if sorted_by_name_employees is not None:
                for employee in sorted_by_name_employees:
                    employee.display()
            else:
                print("No employees found.")

        elif choice == "9":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()