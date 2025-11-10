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

