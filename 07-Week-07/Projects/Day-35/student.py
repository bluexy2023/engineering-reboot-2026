# student.py
# defines the class Student, which represents one student

class Student:
    def __init__(
        self,
        student_id: str,
        first_name: str,
        last_name: str,
        course: str,
        year_level: int,
        gpa: float,
    ):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.year_level = year_level
        self.gpa = gpa

    @property
    def student_id(self):
        return self._student_id
    
    @student_id.setter
    def student_id(self, value):
        if not isinstance(value, str):
            raise ValueError("Student ID must be a string.")
        self._student_id = value

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise ValueError("First name must be a string.")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Last name must be a string.")
        self._last_name = value

    @property
    def course(self):
        return self._course
    
    @course.setter
    def course(self, value):
        if not isinstance(value, str):
            raise ValueError("Course must be a string.")
        self._course = value

    @property
    def year_level(self):
        return self._year_level
    
    @year_level.setter
    def year_level(self, value):
        if not isinstance(value, int):
            raise ValueError("Year level must be an integer.")
        # Range invariant (1 to 5)
        if not (1 <= value <= 5):
            raise ValueError(f"Year level must be between 1 and 5.")
        
        self._year_level = value

    @property
    def gpa(self):
        return self._gpa
    
    @gpa.setter
    def gpa(self, value):
        if not isinstance(value, float):
            raise ValueError("GPA must be a float.")
        # Range invariant (0.0 to 4.0)
        if not (0.0 <= value <= 4.0):
            raise ValueError(f"GPA must be between 0.0 and 4.0.")
        
        self._gpa = value

    def display(self):
        print("-"*30)
        print(f"{'Student ID':<12}: {self.student_id}")
        print(f"{'First Name':<12}: {self.first_name}")
        print(f"{'Last Name':<12}: {self.last_name}")
        print(f"{'Course':<12}: {self.course}")
        print(f"{'Year Level':<12}: {self.year_level}")
        print(f"{'GPA':<12}: {self.gpa}")

    def update(self, student_id=None, first_name=None, last_name=None, course=None, year_level=None, gpa=None):
        """
        Attempts an atomic update on student attributes.
        Returns True if update succeeds, False if any validation fails.
        """
        # 1. Merge incoming inputs with existing state
        proposed_student_id = student_id if student_id is not None else self.student_id
        proposed_first_name = first_name if first_name is not None else self.first_name
        proposed_last_name  = last_name  if last_name  is not None else self.last_name
        proposed_course     = course     if course     is not None else self.course
        proposed_year_level = year_level if year_level is not None else self.year_level
        proposed_gpa        = gpa        if gpa        is not None else self.gpa

        try:
            # 2. Gatekeeper: __init__ runs all property setters on proposed values
            dummy = Student(
                student_id=proposed_student_id,
                first_name=proposed_first_name,
                last_name=proposed_last_name,
                course=proposed_course,
                year_level=proposed_year_level,
                gpa=proposed_gpa
            )

            # 3. Commit: If dummy creation didn't raise an exception, apply changes
            self.student_id = proposed_student_id
            self.first_name = proposed_first_name
            self.last_name  = proposed_last_name
            self.course     = proposed_course
            self.year_level = proposed_year_level
            self.gpa        = proposed_gpa
            
            return True

        except (ValueError, TypeError) as e:
            # Optional: Print the error or log it if needed
            # print(f"Update failed: {e}")
            return False
        

