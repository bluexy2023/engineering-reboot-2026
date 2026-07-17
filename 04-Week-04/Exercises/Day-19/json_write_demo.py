# json writing demo progam to exercise
# dumping a dictionary to a jason file
# import json to use json functionalities
import json

person = {
"name": "Glenn",
"age": 53,
"city": "Newark",
"skills": [
"Python",
"Git",
"Docker"
]
}

# writing to a file
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

