# engineering filter program
# extract information from a CSV, and 
# display only information that matches a certain criteria

engineering_names=[]
number_engineers=0
with open("employees.txt", "r") as file:
    for line in file:
        line = line.rstrip("\n")
        fields = line.split(",")

        if (fields[1] == "Engineering"):
            print(f"{fields[0]:<15} {fields[2]:>10}")
            number_engineers += 1
# stretch assignment
print("Total Engineering Employees:", number_engineers)
# challenge enhancement -- list comprehension
with open("employees.txt", "r") as file:
    engineering_names = [
        line.rstrip("\n").split(",")[0] 
        for line in file
        if line.rstrip("\n").split(",")[1] == "Engineering"
    ]

print (engineering_names)