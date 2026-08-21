# employee.py
# contains the class definitions of Employee, SalariedEmployee, and HourlyEmployee

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

    def display_info(self):
        super().display_info()
        print("Annual Salary:", self.annual_salary)

class HourlyEmployee(Employee):
    def __init__(self, employee_id, name, hourly_rate, hours_worked):
        super().__init__(employee_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def display_info(self):
        super().display_info()
        print("Hourly Rate:", self.hourly_rate)
        print("Hours Worked:", self.hours_worked)