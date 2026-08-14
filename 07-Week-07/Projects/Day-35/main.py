# main program
from helper_utilities import *
from student import Student
from student_directory import StudentDirectory

directory = StudentDirectory()

"""Responsible only for

user interface
menu
input
calling StudentDirectory methods

No business logic should exist here.
"""

"""
1 Add Student

2 Remove Student

3 Update Student

4 Find Student by ID

5 Search by Last Name

6 Display All Students

7 Display Students by Course

8 Highest GPA

9 Lowest GPA

10 Academic Summary

0 Exit
"""

def add_student():
    print("\n- Add Student -")
    student_id = read_input(
        prompt="Enter Student ID: ",
        predicate=lambda s: len(s) > 0,
        error_message="Student ID cannot be blank!"
    )
    first_name = read_input(
        prompt="Enter First Name: ",
        predicate=lambda s: len(s) > 0,
        error_message="First name cannot be blank!"
    )
    last_name = read_input(
        prompt="Enter Last Name: ",
        predicate=lambda s: len(s) > 0,
        error_message="Last name cannot be blank!"
    )
    course = read_input(
        prompt="Enter Course: ",
        predicate=lambda s: len(s) > 0,
        error_message="Course cannot be blank!"
    )
    year_level = read_input(
        prompt="Enter Year Level (1-5): ",
        converter=int,
        predicate=lambda x: 1 <= x <= 5,
        error_message="Year level must be an integer between 1 and 5."
    )
    gpa = read_input(
        prompt="Enter GPA (0.0 - 4.0): ",
        converter=float,
        predicate=lambda x: 0.0 <= x <= 4.0,
        error_message="GPA must be a float between 0.0 and 4.0."
    )

    new_student = Student(student_id, first_name, last_name, course, year_level, gpa)
    if directory.add_student(new_student):
        print("Student added successfully.")

def remove_student():
    print("\n- Remove Student -")
    student_id = read_input(
        prompt="Enter Student ID to remove: ",
        predicate=lambda s: len(s) > 0,
        error_message="Student ID cannot be blank!"
    )
    if directory.remove_student(student_id):
        print("Student removed successfully.")

def update_student():
    print("\n- Update Student -")
    student_id = read_input(
        prompt="Enter Student ID to update: ",
        predicate=lambda s: len(s) > 0,
        error_message="Student ID cannot be blank!"
    )
    student = directory.find_by_id(student_id)
    if not student:
        print("Student not found.")
        return

    first_name = read_input(
        prompt=f"Enter First Name [{student.first_name}]: ",
        predicate=lambda s: len(s) > 0,
        error_message="First name cannot be blank!"
    )
    last_name = read_input(
        prompt=f"Enter Last Name [{student.last_name}]: ",
        predicate=lambda s: len(s) > 0,
        error_message="Last name cannot be blank!"
    )
    course = read_input(
        prompt=f"Enter Course [{student.course}]: ",
        predicate=lambda s: len(s) > 0,
        error_message="Course cannot be blank!"
    )
    year_level = read_input(
        prompt=f"Enter Year Level (1-5) [{student.year_level}]: ",
        converter=int,
        predicate=lambda x: 1 <= x <= 5,
        error_message="Year level must be an integer between 1 and 5."
    )
    gpa = read_input(
        prompt=f"Enter GPA (0.0 - 4.0) [{student.gpa}]: ",
        converter=float,
        predicate=lambda x: 0.0 <= x <= 4.0,
        error_message="GPA must be a float between 0.0 and 4.0."
    )

    if directory.update_student(student_id, first_name=first_name, last_name=last_name, course=course, year_level=year_level, gpa=gpa):
        print("Student updated successfully.")
    else:
        print("Failed to update student.")

def find_student_by_id():
    print("\n- Find Student by ID -")
    student_id = read_input(
        prompt="Enter Student ID to find: ",
        predicate=lambda s: len(s) > 0,
        error_message="Student ID cannot be blank!"
    )
    student = directory.find_by_id(student_id)
    if student:
        student.display()
    else:
        print("Student not found.")

def search_by_last_name():
    print("\n- Search by Last Name -")
    last_name = read_input(
        prompt="Enter Last Name to search: ",
        predicate=lambda s: len(s) > 0,
        error_message="Last name cannot be blank!"
    )
    students = directory.find_by_last_name(last_name)
    if students:
        for student in students:
            student.display()
    else:
        print("No students found with that last name.")

def display_all_students():
    print("\n- Display All Students -")
    directory.display_all()

def display_students_by_course():
    print("\n- Display Students by Course -")
    course = read_input(
        prompt="Enter Course to display: ",
        predicate=lambda s: len(s) > 0,
        error_message="Course cannot be blank!"
    )
    students = directory.students_by_course(course)
    if students:
        for student in students:
            student.display()
    else:
        print("No students found in that course.")

def display_highest_gpa():
    print("\n- Highest GPA -")
    student = directory.highest_gpa()
    if student:
        print(f"Highest GPA: {student.gpa}")
        student.display()
    else:
        print("No students available.")

def display_lowest_gpa():
    print("\n- Lowest GPA -")
    student = directory.lowest_gpa()
    if student:
        print(f"Lowest GPA: {student.gpa}")
        student.display()
    else:
        print("No students available.")

def display_academic_summary():
    print("\n- Academic Summary -")
    directory.academic_summary()

def exit_program():
    print("\nGoodbye!")
    return "EXIT"  # Signal to the menu loop to stop


def main():
    main_menu = ConsoleMenu("Student Directory Menu")
    main_menu.add_option("1", "Add Student", add_student)
    main_menu.add_option("2", "Remove Student", remove_student)
    main_menu.add_option("3", "Update Student", update_student)
    main_menu.add_option("4", "Find Student by ID", find_student_by_id)
    main_menu.add_option("5", "Search by Last Name", search_by_last_name)
    main_menu.add_option("6", "Display All Students", display_all_students)
    main_menu.add_option("7", "Display Students by Course", display_students_by_course)
    main_menu.add_option("8", "Highest GPA", display_highest_gpa)
    main_menu.add_option("9", "Lowest GPA", display_lowest_gpa)
    main_menu.add_option("10", "Academic Summary", display_academic_summary)
    main_menu.add_option("0", "Exit", exit_program)
    main_menu.run()

if __name__ == "__main__":
    main()
