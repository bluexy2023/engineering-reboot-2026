## main.py ######################################################
# a python application that uses the Employee class from 
# the employee module. The application should:
# - Create multiple Employee objects.
# - Store them in a collection.
# - Iterate through the collection.
# - Invoke methods on each object.
# - Demonstrate independent object state.
# - Display formatted employee information.
#################################################################
from employee import Employee

# let's create 3 instances of the Employee class
employee1 = Employee(1001,"Randy","Jackson", "Marketing", "Team Leader",90000,2024 )
employee2 = Employee(1002,"Glenn","Ogapong", "Engineering", "Scrum Master",100000,2023 )
employee3 = Employee(1003,"Lea","Rodriguez", "Finance", "Manager",120000,2015 )

# let's store our instances (objects) in a collection
employees = [employee1, employee2, employee3]

# iterate and perform methods from each one
for employee in employees:
    # display information:
    employee.display_information()
    # get years of service from each one
    print(f"Years of Service: {employee.calculate_years_of_service()}")

# HR has announced that the company has decided to give a raise of 5000 across the board 
# due to the meeting the 2026 midyear targets
print(f"Increasing salary of each employee by 5000.")
for employee in employees:
    # let's give a raise of 5000 each (lucky!)
    employee.give_raise(5000)
    # now, let's see how their information have changed individually. Pay close
    # attention to their salaries
    employee.display_information()