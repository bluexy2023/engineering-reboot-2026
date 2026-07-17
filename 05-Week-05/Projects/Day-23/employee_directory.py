# employee directory management system
# mini project for day 23

from employee_data import EMPLOYEES as employees

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

def display_employee(employee: dict) -> None:
    for key, value in employee.items():
        print(f"{key}: {value}")

def search_employee(emp_id: int) -> dict:
    for employee in employees:
        if employee["id"] == emp_id:
            return employee
        
    return None

def search_employee_by_name(name: str) -> dict:
    for employee in employees:
        if employee["name"].lower() == name.lower():
            return employee
    return None

def get_employee_count() -> int:
    return len(employees)

def employees_by_department(department: str) -> list[dict]:
    return [employee for employee in employees if employee["department"].lower() == department.lower()]

def average_salary() -> float:
    if not employees:
        return 0.0
    total_salary = sum(employee["salary"] for employee in employees)
    return total_salary / len(employees)

def highest_salary_employee() -> dict:
    if not employees:
        return None
    return max(employees, key=lambda emp: emp["salary"])

def sort_employees_by_salary() -> list[dict]:
    return sorted(employees, key=lambda emp: emp["salary"], reverse=True)

def sort_employees_by_name() -> list[dict]:
    return sorted(employees, key=lambda emp: emp["name"].lower())







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
    while True:
        print_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            emp_id = read_id("Enter Employee ID: ")
            employee = search_employee(emp_id)
            if employee:
                display_employee(employee)
            else:
                print("Employee not found.")

        elif choice == "2":
            name = read_name("Enter Employee Name: ")
            employee = search_employee_by_name(name)
            if employee:
                display_employee(employee)
            else:
                print("Employee not found.")

        elif choice == "3":
            count = get_employee_count()
            print(f"Total number of employees: {count}")

        elif choice == "4":
            department = read_name("Enter Department Name: ")
            dept_employees = employees_by_department(department)
            if dept_employees:
                for emp in dept_employees:
                    display_employee(emp)
                    print("-" * 20)
            else:
                print("No employees found in this department.")

        elif choice == "5":
            avg_salary = average_salary()
            print(f"Average salary: ${avg_salary:.2f}")

        elif choice == "6":
            highest_employee = highest_salary_employee()
            if highest_employee:
                display_employee(highest_employee)
            else:
                print("No employees found.")

        elif choice == "7":
            sorted_employees = sort_employees_by_salary()
            for emp in sorted_employees:
                display_employee(emp)

        elif choice == "8":
            sorted_employees = sort_employees_by_name()
            for emp in sorted_employees:
                display_employee(emp)

        elif choice == "9":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()