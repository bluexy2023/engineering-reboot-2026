# set manipulation using the data from employee_data.py
# exercise 2 for day 23
from employee_data import EMPLOYEES as employees


#Create a set named departments containing every department found in the employee records.
#Display the contents of the set.
#Display the total number of unique departments.
#Verify that duplicate departments (for example, Engineering) appear only once.
#Prompt the user to enter a department name.
#Determine whether that department exists in the set.
#Display an appropriate message indicating whether the department exists.
#Add a new department (for example, "Legal").
#Display the updated set.
#Remove the newly added department.
#Display the final set.
departments = set()
for employee in employees:
    departments.add(employee["department"])

print(f"Departments: {departments}")
print(f"Total Unique Departments: {len(departments)}")

while True:
    user_input = input("Enter a department:")
    if user_input in departments:
        print(f"{user_input} exists in the set.")
    else:
        print(f"{user_input} does not exist in the set.")
        break
# add "Legal" department
departments.add("Legal")
print(f"Updated Departments: {departments}")
# remove "Legal" department
departments.remove("Legal")
print(f"Final Departments: {departments}")
                    