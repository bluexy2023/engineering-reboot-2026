# main.py
# exercises the employee.py module by creating instances of the classes and calling their methods

from employee import Employee, SalariedEmployee, HourlyEmployee

def main():
    # Create an instance of Employee
    emp1 = Employee(1, "John Doe")
    emp1.display_info()
    print()

    # Create an instance of SalariedEmployee
    salaried_emp = SalariedEmployee(2, "Jane Smith", 60000)
    salaried_emp.display_info()
    print()

    # Create an instance of HourlyEmployee
    hourly_emp = HourlyEmployee(3, "Mike Johnson", 20, 40)
    hourly_emp.display_info()
    print()

if __name__ == "__main__":
    main()