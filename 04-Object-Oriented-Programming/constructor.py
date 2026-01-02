# ======= Constructor in Python =======
"""
    -> A constructor is a special method that is automatically called when an object of a class is created.
    -> The primary purpose of a constructor is to initialize the attributes of the newly created object.
    -> In Python, the constructor method is defined using the __init__() method.
    -> The __init__() method can take parameters to initialize the object's attributes with specific values when the object is created.

"""

class Person:
    def __init__(self, name, age):
        self.name = name  # Initializing the name attribute
        self.age = age    # Initializing the age attribute

    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
# Creating an object of the Person class
person1 = Person("Eren", 21)
print(person1.introduce()) 

# Creating another object of the Person class
person2 = Person("Mikasa", 20)
print(person2.introduce())

# Accessing attributes directly
print(person1.name)
print(person2.age)

# Modifying attributes directly
person1.age = 31
print(person1.introduce())

# Note: The __init__() method is not mandatory in a class. If you do not define it, Python will provide a default constructor that does nothing.
# Example of a class without an explicit constructor
class EmptyClass:
    pass
empty_object = EmptyClass()
print(empty_object)  # Output: <__main__.EmptyClass object at ...>
# You can still add attributes to the object after its creation
empty_object.new_attribute = "I am new"
print(empty_object.new_attribute) 




