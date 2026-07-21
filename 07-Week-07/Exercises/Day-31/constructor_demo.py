# my first python class with __init__

class Person:
    # __init__ takes the paremeters passed to it (always +1)
    # as first parameter is assigned to a pointer to the class
    # itself.  __init__ takes an instance of itself and creates
    # an 'instance' variable (the internal data that belongs to the 
    # object itself)
    def __init__(self, name, age):
        self.name = name
        self.age = age


# let's instantiate multiple Person objects

person1 = Person("Glenn John", 53)
person2 = Person("Thotho Genoves", 35)


print("Person1:")
print(f"\tName:\t{person1.name}")
print(f"\tAge:\t{person1.age}")
print("\nPerson2:")
print(f"\tName:\t{person2.name}")
print(f"\tAge:\t{person2.age}")

