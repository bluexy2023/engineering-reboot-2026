# score processor program
# Exercise 2 of Day 14

scores = [88, 92, 76, 81, 95, 67]

## statistical processing and conditional counting
# get average
# get highest
# get lowest 
# number of students who passed (70 and above)

average_score = sum(scores) / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

# get number of students who passed
# get number who scored 90+
number_passed=0 # initialize
exceptional_number=0
for score in scores:
    if score >= 70:
        number_passed += 1
        if score > 90:
            exceptional_number += 1
print("Average Score:", average_score)
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
print("Number Passed:", number_passed)
print("Exceptional Number", exceptional_number)


