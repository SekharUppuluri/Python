# ===== Modules =====
# Modules are files containing Python code that can be imported and used in other Python programs.
# They help organize code into manageable sections and promote code reuse.

# Importing a module
import math 
print("Using math module:")
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)
# Importing specific functions from a module
from math import factorial, pow
print("Factorial of 5:", factorial(5))
print("2 raised to the power 3:", pow(2, 3))

import keyword
print(keyword.kwlist)
print("Number of keywords in Python:", len(keyword.kwlist)) 

import random
print("Random number between 1 and 10:", random.randint(1, 10))
print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry']))

import datetime
now = datetime.datetime.now()
print("Current date and time:", now)
print("Current year:", now.year)
print("Current month:", now.month)
print("Current day:", now.day)

help('modules')  # Lists all available modules

# This concludes the basics of modules in Python.