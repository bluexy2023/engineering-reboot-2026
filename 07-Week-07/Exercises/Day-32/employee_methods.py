# employee_methods.py
# Exercise 1 of Day 31

class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary


    def display_information(self):
        for key, value in self.__dict__.items():
            print(f"{key.replace('_',' ').title():<12}:{value}")

    def get_annual_salary(self):
        return self.salary

    def apply_raise(self,percentage):
        self.salary += percentage * self.salary / 100

    def transfer_department(self,new_department):
        self.department = new_department


if __name__ == "__main__":
    emp1 = Employee(1001,"Glenn", "Engineering", 120000)
    emp1.display_information()
    print(f"Annual Salary: {emp1.get_annual_salary()}")
    emp1.apply_raise(10)
    emp1.transfer_department("Marketing")
    emp1.display_information()