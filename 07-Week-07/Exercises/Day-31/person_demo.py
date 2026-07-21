# my first python class

class Person:
    pass

# let's instantiate multiple Person objects

person1 = Person()
person2 = Person()
person1.name = "Glenn John"
person1.age = 53
person2.name = "Thotho Genoves"
person2.age = 35

print("Person1:")
print(f"\tName:\t{person1.name}")
print(f"\tAge:\t{person1.age}")
print("\nPerson2:")
print(f"\tName:\t{person2.name}")
print(f"\tAge:\t{person2.age}")

