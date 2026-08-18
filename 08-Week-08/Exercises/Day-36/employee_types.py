# employee_types.py
class Employee:
    def __init__(self,employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_info(self):
        print(self.employee_id, self.name)

class SalariedEmployee(Employee):
    def get_type(self):
        return "Salaried Employee"

class HourlyEmployee(Employee):
    def get_type(self):
        return "Hourly Employee"

if __name__ == "__main__":
    emp1 = Employee(1, "John Doe")
    emp1.display_info()

    salaried_emp1 = SalariedEmployee(2, "Jane Smith")
    salaried_emp1.display_info()
    print(salaried_emp1.get_type())

    salaried_emp2 = SalariedEmployee(3, "Alice Johnson")
    salaried_emp2.display_info()
    print(salaried_emp2.get_type())

    hourly_emp1 = HourlyEmployee(4, "Bob Brown")
    hourly_emp1.display_info()
    print(hourly_emp1.get_type())