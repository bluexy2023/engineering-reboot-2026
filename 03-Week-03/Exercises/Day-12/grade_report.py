# grade report python program
# Exercise 3 of Day 12

# let's create our list of grades
grades = [88,92,79,95,84]

# use a foor loop to:
# -- Display each grade in the format
#    Grades: Grade1, Grade2, ..., Graden-1
# -- Count grades
# -- Calculate average

gradesString=""
totalGrades=0
for grade in grades:
    # build gradeString
    # check if totalGrades is already != 0
    # -- meaning, this is not the first grade in the list
    if totalGrades != 0:
        gradeString += ", " + str(grade)
    else:
        gradeString=str(grade)
    totalGrades += grade
# display each grade as a string series
print("Grades: " + gradeString)
# Count grades
print("Count:",len(grades))

# print average grade
print("Average: " + str(float(totalGrades / len(grades))))
        