# student_directory.py
# defines the StudentDirectory class, which manages a collection of Student objects
# the following will be the methods of the StudentDirectory class:
"""add_student()

remove_student()

update_student()

find_by_id()

find_by_last_name()

display_all()

students_by_course()

academic_summary()

highest_gpa()

lowest_gpa()"""

from student import Student

class StudentDirectory:
    def __init__(self):
        self._students = []
        self._students_by_id_dict = {}

    def add_student(self, student):
        if student.student_id in self._students_by_id_dict:
            print("Student with this ID already exists.")
            return False
        self._students.append(student)
        self._students_by_id_dict[student.student_id] = student
        return True
    
    def remove_student(self, student_id):
        student_to_remove = self.find_by_id(student_id)
        if student_to_remove:
            self._students.remove(student_to_remove)
            del self._students_by_id_dict[student_id]
            return True
        print("Student not found.")
        return False
    
    def update_student(self, student_id, **kwargs):
        student = self.find_by_id(student_id)
        if student:
            return student.update(student_id=student_id, **kwargs)
        print("Student not found.")
        return False
    
    def find_by_id(self, student_id):
        return self._students_by_id_dict.get(student_id, None)
    
    def find_by_last_name(self, last_name):
        return [s for s in self._students if s.last_name.lower() == last_name.lower()] 

    def display_all(self):
        for student in self._students:
            student.display()

    def students_by_course(self, course):
        return [s for s in self._students if s.course.lower() == course.lower()] 

    def academic_summary(self):
        print("-" * 30)
        # Guard clause: handle empty directory upfront
        if not self._students:
            print("No student records found.")
            print("-" * 30)
            return

        # Safe to compute statistics now
        avg_gpa = sum(s.gpa for s in self._students) / len(self._students)
    
        print(f"{'Total Students':<15}: {len(self._students)}")
        print(f"{'Average GPA':<15}: {avg_gpa:.2f}")
    
        print("Number of Students per Course:")
        course_counts = {}
        for student in self._students:
            course_counts[student.course] = course_counts.get(student.course, 0) + 1
        for course, count in course_counts.items():
            print(f"  {course:<13}: {count}")

        print(f"{'Highest GPA':<15}: {self.highest_gpa().gpa}")
        print(f"{'Lowest GPA':<15}: {self.lowest_gpa().gpa}")
        
      

    def highest_gpa(self):
        if not self._students:
            return None
        return max(self._students, key=lambda s: s.gpa)

    def lowest_gpa(self):
        if not self._students:
            return None
        return min(self._students, key=lambda s: s.gpa)

    
