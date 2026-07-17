# json read demo program 
# exercise 2 of day 19
# program to read json data into memory and displaying its contents
import json
# open file
data=None
with open("person.json", "r") as file:
    data = json.load(file)
    for name,value in data.items():
        if isinstance(value, list):
            print (name,":")
            for skill in value:
                print("     ",skill)
            # exercise 4
            # add "VSCode" in the skill
            value.append("VSCode")
        else:
            print (f"{name:<15}:{value}")

# at this point our data should have an updated version of the skills
# now let's open the person data for writing and dump our data into it
with open("person.json", "w") as file:
    json.dump(data,file,indent=4)
    