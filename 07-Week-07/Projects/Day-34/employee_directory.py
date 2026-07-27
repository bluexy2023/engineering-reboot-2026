# class EmployeeDirectory
# is a collection manager for Employee objects
from employee import Employee
class EmployeeDirectory:
    # Initializes the _employees list to an empty collection
    def __init__(self):
        self._employees: list[Employee] = []

    # Load data from somewhere. This takes a list of dictionaries
    def load_data(self, employee_list: list[dict]):
        for emp in employee_list:
            # let's create a new Employee instance for each 
            # employee dictionary from our employee list
            employee = Employee(**emp)
            self._employees.append(employee)

    # Employee search by ID from the collection of Employee objects
    def search_by_id(self,id) -> Employee | None:
        for employee in self._employees:
            if employee.id == id:
                return employee
        return None
    
    # Employee search by non case-sensitive name from the collection of Employee objects
    def search_by_name(self,name) -> Employee | None:
        for employee in self._employees:
            if employee.name.lower() == name.lower():
                return employee
        return None
    
    # Get a collection of Employee objects grouped by department
    def get_by_department(self,department) -> list[Employee]:
        return [
            employee
            for employee in self._employees
            if employee.department.lower() == department.lower()
        ]
        

    # Compute for the average salary
    def get_average_salary(self) -> float:
        if self._employees:
            total_salary = sum(employee.salary for employee in self._employees)
            return total_salary / self.get_count()
        return 0.0

    # Retrieve the Employee object with the highest salary
    def get_highest_paid(self) -> Employee | None:
        if self._employees:
            return max(self._employees, key=lambda employee: employee.salary)
        return None

    # Get a collection of Employee objects sorted by salary in descending order.
    def sort_by_salary(self) -> list[Employee] | None:
        if self._employees:
            return sorted(self._employees, key=lambda employee: employee.salary, reverse=True)
        return None

    # Get a collection of Employee objects sorted by name in ascending order.
    def sort_by_name(self) -> list[Employee] | None:
        if self._employees:
            return sorted(self._employees, key=lambda employee: employee.name.lower())
        return None

    # Retrieve the count of Employee objects from the list of Employee objects in this EmployeeDirectory instance
    def get_count(self) -> int:
        return len(self._employees)

