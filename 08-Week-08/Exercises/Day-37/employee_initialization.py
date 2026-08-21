# employee_initialization.py
class Employee:
    def __init__(self,employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_info(self):
        print(self.employee_id, self.name)

class SalariedEmployee(Employee):
    def __init__(self, employee_id, name, annual_salary):
        super().__init__(employee_id, name)
        self.annual_salary = annual_salary

    

class HourlyEmployee(Employee):
    def __init__(self, employee_id, name, hourly_rate, hours_worked):
        super().__init__(employee_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked   


if __name__ == "__main__":
    employee = Employee(1, "John Doe")
    salaried_employee = SalariedEmployee(2, "Jane Smith", 60000)
    hourly_employee = HourlyEmployee(3, "Mike Johnson", 20, 40)
    employee.display_info()
    salaried_employee.display_info()
    hourly_employee.display_info()