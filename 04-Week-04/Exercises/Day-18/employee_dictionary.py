# employee dictionary program
# exercise 2 of day 18

# exercise to create a collection of dictionaries for the employee record
# - "name"
# - "department"
# - "salary"

employees = []

# open our employees.txt file and process each line to extract info
# into a dictionary
with open("employees.txt", "r") as file:
    for line in file:
        employee_record = line.rstrip("\n").split(",")
        employee = {
            "name": employee_record[0],
            "department": employee_record[1],
            "salary" : employee_record[2]
        }
        employees.append(employee)
print("Employee Records")
print(employees)

## enhancement 1
# create department summary
dept_summary = {}
for employee in employees:
    # check if this department name is in our disctionary
    # if so, increment its count
    if employee["department"] in dept_summary:
        dept_summary[employee["department"]] += 1
    # otherwise, set its initial value to one as this is the first
    # time it is seen
    else:
        dept_summary[employee["department"]] = 1
    
# print department summary
## This first solution works, and is correct
## this iterates through all the keys of the dictionary
## and use it to look up the dictionary to get the counts
print("\nDepartment Summary\n")
for department in dept_summary.keys():
    # use formatting for print
    # print(f"{department:<15}: {count}")
    print(f"{department:<15}:{dept_summary[department]}")
          
# 2nd solution
# uses items, and this is a more pythonic approach
# and more efficient as items() generates a list of name-value pair
# no secondary lookup required
print("\nDepartment Summary: 2nd Solution")
for deparment, count in dept_summary.items():
    print(f"{department:<15}:{count}")

## enhancement 2
# high salary report
# display employees earning 80000 or more
print ("\nHigh Salary employees:\n")
for employee in employees:
    if int(employee["salary"]) >= 80000:
        print(employee["name"])
 

