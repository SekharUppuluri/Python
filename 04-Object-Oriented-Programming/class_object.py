# ======= Class and Object  =======
"""
    class : A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
    object : An instance of a class. It is created using the class blueprint and can have its own unique attributes and behaviors.
"""

class aot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def attack(self):
        return "Take that!"

# ======= Creating Object Instances =======
eren_instance = aot("Eren Yeager", 15)
print(eren_instance.name) 
print(eren_instance.age)  
print(eren_instance.attack())  



