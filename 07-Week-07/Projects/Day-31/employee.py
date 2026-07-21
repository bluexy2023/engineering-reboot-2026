# Employee class that defines a class objects with the following 
# states:
#   employee_id
#   first_name
#   last_name
#   department
#   position
#   salary
#   hire_year
# and with the following behaviors:
#   display_information()
#   give_raise()
#   transfer_department()
#   update_position()
#   calculate_years_of_service()
#   full_name()
from datetime import date

class Employee:
    attribute_to_name_mapping = {
        "employee_id"   :   "Employee ID",
        "first_name"    :   "First Name",
        "last_name"     :   "Last Name",
        "department"    :   "Department",
        "position"      :   "Position",
        "salary"        :   "Salary",
        "hire_year"     :   "Hire Year"
    }
    def __init__(self,employee_id,first_name,
               last_name, department, position,
               salary, hire_year):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.position = position
        self.salary = salary
        self.hire_year = hire_year

    def display_information(self):
        for attribute, value in self.__dict__.items():
            print(f"{self.__class__.attribute_to_name_mapping[attribute]:<12}: {value}")

    def give_raise(self, raise_amount):
        self.salary += raise_amount

    def transfer_department(self,new_department):
        self.department = new_department

    def update_position(self,new_position):
        self.position = new_position

    def calculate_years_of_service(self):
        return (date.today().year - self.hire_year)
    
    def full_name(self):
        return (self.first_name + " " + self.last_name)
    

## test code here ##
if __name__ == "__main__":
    emp1 = Employee(1001,"Glenn John","Ogapong", "Engineering", "Team Leader",120000,2024 )

    # let's display emp1 information
    emp1.display_information()

    # let's get the fullname:
    print(f"Employee 1 Full Name: {emp1.full_name()}")

    # let's give employee 1 a raise
    emp1.give_raise(100)

    emp1.display_information()

    # years of service
    print(f'Years of service: {emp1.calculate_years_of_service()}')

    # let's transfer to a different department
    emp1.transfer_department("Marketing")
    # let's update his position
    emp1.update_position("Manager")
    emp1.display_information()