# Employee Analytics program for Day 18

employee_list = []
# Step 1, Read employees.txt
with open("employees.txt", "r") as file:

    # Step 2
    # Convert each record into a dictionary and store all employee dictionary in a list

    for line in file:
        line = line.rstrip("\n")
        employee_record_list=line.split(",")
        employee_record = {
            "name" : employee_record_list[0],
            "department" : employee_record_list[1],
            "salary" : int(employee_record_list[2])
        }
        employee_list.append(employee_record)

# Generate Total Employees
employees_total = len(employee_list)
print("Total Employees:", employees_total)

# step 4, generate department total
dept_summary = {}
for employee in employee_list:
    if employee["department"] in dept_summary:
        dept_summary[employee["department"]] += 1
    else:
        dept_summary[employee["department"]] = 1
print("\nDepartment Totals:")
for department_name, total in dept_summary.items():
    print (f"{department_name:<15}:{total}")

# Step 5: Determine the higest paid employee
salaries = [employee["salary"] for employee in employee_list]
max_salary=max(salaries)
for employee in employee_list:
    if employee["salary"] == max_salary:
        print("Highest Paid Employee:\n")
        print(employee["name"])
        print(max_salary)

# Step 6
# Calculate average Salary
salary_average = sum(salaries) / employees_total;
print("Average Salary:", salary_average)

## Enhancement 1
# high earner's report
# display all employees earning 90000 or greater
# list comprehension exercise below
high_earners=[employee["name"] for employee in employee_list if employee["salary"] >= 90000]
print("\nHigh Earners:\n")
for name in high_earners:
    print(name)

## Enhancement 2
# display Engineering Employee Count and Engineering Average Salary
engineering_salaries=[employee["salary"] for employee in employee_list if employee["department"] == "Engineering"]
print("\nEngineering Analysys:\n")
print("Employees:", len(engineering_salaries))
print("Average Salary:", sum(engineering_salaries) / len(engineering_salaries))

## Challenge Enhancement
# Generate a report sorted by salary from highest to loweest
def get_salary(employee):
    return employee["salary"]

salary_ranking = sorted(
    employee_list,
    key=get_salary,
    reverse=True
)
print("\nSalary Ranking\n")
for employee in salary_ranking:
    print(employee["name"],employee["salary"])
