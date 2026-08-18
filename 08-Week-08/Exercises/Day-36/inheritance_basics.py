# inheritance_basics.py
class Employee:
    def __init__(self,employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_info(self):
        print(self.employee_id, self.name)


class SalariedEmployee(Employee):
    pass


if __name__ == "__main__":
    emp1 = Employee(1, "John Doe")
    emp1.display_info()

    salaried_emp1 = SalariedEmployee(2, "Jane Smith")
    print(salaried_emp1.employee_id)
    print(salaried_emp1.name)
    salaried_emp1.display_info()