# student manager to display all students
# search student by ID and display information
# add student
# save changes
import json
def display_menu():
    print("\n1. Display all students")
    print("2. Seach student:")
    print("3. Add Student")
    print("4. Quit with saving\n")

def display_allStudents(data):
    print ("\nAll students")
    print("==============")
    for student in data:
        for key,value in student.items():
            print(key,":", value)

def search_student(id,data):
    student_found=False
    for student in data:
        if (student["id"] == int(id)):
            print("Student Found!")
            student_found=True
            for key,value in student.items():
                print(key,":",value)
    if (not student_found):
        print("Student NOT found!!!")

def add_student(data):
    id=input("Enter ID:")
    name=input("Enter Name:")
    course=input("Enter Course:")
    gpa=input("Enter GPA:")
    new_student={
        "id" : int(id),
        "name": name,
        "course" : course,
        "gpa" : int(gpa)
    }
    data.append(new_student)

def save_record(data,filename):
    # perform save, if any
    with open(filename, "w") as file:
        json.dump(data,file,indent=4)

## main routine 
json_filename="students.json"
data=None # initialize data into None, but make it global
with open(json_filename, "r") as file:
    data = json.load(file)
while True:
    display_menu()
    selection = int(input("Enter Selection:"))
    if selection == 1:
        display_allStudents(data)
    elif selection == 2:
        id=input("Enter student ID:")
        search_student(id, data)
    elif selection == 3:
        add_student(data)
    elif selection == 4:
        save_record(data,json_filename)
        break
    else:
        print("Invalid Selection!")
        continue

                 
    