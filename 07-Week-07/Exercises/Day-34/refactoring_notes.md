</MARKDOWN>

# Refactoring notes for employee_directory.py

1. Duplicated Code
  - reports can be made generic.  Could be an opportunity for a class
    with a method (generate_report, with criteria)
  - search could be made more generic
2. Long Functions
  - reports have lots of duplicated code that could be refactored to reduce
    the length of code to simplify the functions
  - search is another area where it could be reduced by the use of lambda functions and reusable code
3. Mixed responsibilities
  - so far, there are no fixed responsibilities in the functions, but there are repeated function calls from within reports that could be reduced
4. Poor naming
   - so far, naming have been good, as this has been practiced early in the reboot, but if they are going to be under a class for reports, sort_employees_by_salary, 'employees' will be removed, and instead the function becomes a method under 'EmployeeCollection', and named "sort_by_salary"
5. Global Data
  - there are other areas of the exercises (not particular to employee_reporting.py) that I used global variables.  
  Ex. validated_registration_system.py
  MINIMUM_AGE = 18
  MAXIMUM_AGE = 65
  MINIMUM_NAME_LENGTH = 2
6. Repeated logic
   - search, reports, repeated use of for loop

Ex. 2.
From employee_directory.py

refactor it into 
a. Data Model (Employee class)
b. EmployeeDirectory (Collection manager)
   all reports will be under this class
   : search_employee_by_name becomes, search_by_name
   : employees_by_department becomes, get_by_department
   "all references to the name 'employees' will be removed
c. DirectoryCLI or ConsoleUI

Ex. 3. Improve naming
  - change average_salary to get_average_salary from EmployeeDirectory
  - sort_employee_by_salary to sort_by_salary under EmployeeDirectory
  - get_employee_count. try implementing __len__ from EmployeeDirectory
  
Ex. 4. Reduce duplication
  - utility like, read_name, read_id, read_chouse, can be a utility
   

   