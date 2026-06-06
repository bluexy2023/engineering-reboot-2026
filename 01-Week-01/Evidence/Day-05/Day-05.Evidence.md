Mardown

# Day 5 Evidence.md
-- git status
----- journal files moved from Notes into the Journal section of that weekly artifacts
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    01-Week-01/Notes/Day-01-Journal.md
        deleted:    01-Week-01/Notes/Day-02-Journal.md
        deleted:    01-Week-01/Notes/Day-03-Journal.md
        deleted:    01-Week-01/Notes/Day-04-Journal.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        01-Week-01/Evidence/Day-05/
        01-Week-01/Exercises/Day-05/
        01-Week-01/Journal/
        01-Week-01/Notes/Day-05-Notes.md
        01-Week-01/Planning/Engineering Reboot 2026 - Week 01 Day 05 Field Manual.pdf

no changes added to commit (use "git add" and/or "git commit -a")


## created Day-05 folder under Exercises

## created calculator.py under Day-05 under Exercises under 01-Week-01

## file content of calculator.py for now

# # Engineering Reboot 2026
# Week 01 Day 05
# Calculator Project

## print a welcome message to the user
## telling it what this program is trying to do
# print("calculator.py implemntation for Engineering # Reboot 2026")

# ask for first number

1st_num = input ("enter the first number:")
2nd_num = input ("enter the second number:")

# source code created to perform Addition, Subtraction, Multiplication, and division

## inputs were converted to 'float' first, then performed operations, and saved to variables

## performed calculations on 3 test cases
PS C:\Projects\Engineering-Reboot-2026\01-Week-01\Exercises\Day-05> python .\calculator.py
calculator.py implemntation for Engineering Reboot 2026
enter the first number:10
enter the second number:5
Addition: 15.0
Subtraction: 5.0
Multiplication: 50.0
Division: 2.0
PS C:\Projects\Engineering-Reboot-2026\01-Week-01\Exercises\Day-05> python .\calculator.py
calculator.py implemntation for Engineering Reboot 2026
enter the first number:20
enter the second number:4
Addition: 24.0
Subtraction: 16.0
Multiplication: 80.0
Division: 5.0
PS C:\Projects\Engineering-Reboot-2026\01-Week-01\Exercises\Day-05> python .\calculator.py
calculator.py implemntation for Engineering Reboot 2026
enter the first number:12.5
enter the second number:2.5
Addition: 15.0
Subtraction: 10.0
Multiplication: 31.25
Division: 5.0

## above were the results