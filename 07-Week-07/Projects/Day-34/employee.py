# class Employee
class Employee:
    def __init__(
        self,
        id: int,
        name: str,
        age: int,
        department: str,
        salary: float,
    ):
        self.id = id
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    # replaces display_employee() 
    def display(self) -> None:
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")
