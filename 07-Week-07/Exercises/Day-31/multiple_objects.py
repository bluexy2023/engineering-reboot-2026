# multiple_objects.py.  

"""Demonstrate independent object state.

Create several Person objects.

Invoke methods on each object.

Verify that modifying one object does not affect the others.
"""

class Person:
    # __init__ takes the paremeters passed to it (always +1)
    # as first parameter is assigned to a pointer to the class
    # itself.  __init__ takes an instance of itself and creates
    # an 'instance' variable (the internal data that belongs to the 
    # object itself)
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_information(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def rename(self, name):
        self.name = name

    def have_birthday(self):
        self.age += 1


# let's instantiate multiple Person objects

person1 = Person("Glenn John", 53)
person2 = Person("Thotho Genoves", 35)
person3 = Person("Lea Ogapong", 51)


person1.display_information()
person1.rename("Mhegs")
person2.display_information()
person2.have_birthday()
person3.have_birthday()
person3.display_information()
person1.display_information()
person2.display_information()


# let's try to access internal info
print(f"person3.name: {person3.name}")

# let's rename person3
person3.rename("Lea Rodriguez Ogapong")
print(f"person3.name: {person3.name}")
person3.display_information()