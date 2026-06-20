# personal data anaylyzer python program
# day 15 coding exercise, which should be an application of
# week 3 learnings

## Objective
#Create a collection of structured personal records 
# and generate a formatted report

people = [
    {
        "name": "Alice",
        "age": 25,
        "city": "New York"
    },
    {
        "name": "Bob",
        "age": 32,
        "city": "Chicago"
    },
    {
        "name": "Charlie",
        "age": 28,
        "city": "Boston"

    },
    {
        "name": "Diana",
        "age": 35,
        "city": "Seattle"
    }
]

# Display records in structure form

#for person in people:
#    print(person)

# Display records in a formatted report form
#for person in people:
#    print("Name: ", person["name"])
#    print("Age:", person["age"])
#    print("City:", person["city"])


## Phase 2: Collection processing and reporting
# Calculate: Total People: Average Age: Youngest Age:
# Oldest Age:
total_people= len(people)

##### let's build our ages collection
ages = [] # initialize collection

# let's iterate through our dictionary collection and parse/extract
# the age attribute of the person object(dictionary)
for person in people:
    ages.append(person["age"])

# Calculate Average age
average_age = sum(ages) / len(ages)
youngest_age = min(ages)
oldest_age = max(ages)

# Display results in a report format
print("Total People:", total_people )
print("Average Age:", average_age)
print("Youngest Age:", youngest_age)
print("Oldest Age:", oldest_age)

# PHASE 3 – CHALLENGE EXTENSION
# People aged 30 and above
# People aged 30 and below
ages_30_and_above = 0
ages_below_30=0
for person in people:
    if person["age"] >= 30:
        ages_30_and_above += 1
    else:
        ages_below_30 += 1
# print results
print("Ages 30 and Above:", ages_30_and_above)
print("Ages below 30:", ages_below_30)


# Phase 4 - Challenge Extension 2
# Create a summary of number of persons living in 
# a city

city_count = {} # create city count name value pair
for person in people:
    city=person["city"]
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1
# print city count object
print(city_count)
# print in report format
print("Persons living in each city summary:")
for city in city_count:
    print(city + ":",city_count[city])

