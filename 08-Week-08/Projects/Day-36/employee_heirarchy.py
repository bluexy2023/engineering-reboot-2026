# employee_heirarchy.py
class Employee:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        
    def display_info(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}")

class SalariedEmployee(Employee):
    def get_type(self):
        return "Salaried Employee"

class HourlyEmployee(Employee):
    def get_type(self):
        return "Hourly Employee"


if __name__ == "__main__":
    employee1 = SalariedEmployee(1, "Alice")
    employee2 = HourlyEmployee(2, "Bob")
    employee1.display_info()
    print(f"Type: {employee1.get_type()}")
    employee2.display_info()
    print(f"Type: {employee2.get_type()}")