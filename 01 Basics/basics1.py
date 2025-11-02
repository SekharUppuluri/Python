# ===== Basics1 of Python =====

# ----- python output, comments, and case sensitivity -----
# python is a case-sensitive language
print("Hello, World!")
# Print("Hello, World!")  # This will raise an error
print('Eren Yeager')
print(3.14, 42, True)
print(5, 10, 15 , sep='-')
print(5, 10, 15 , sep='/')
print(5, 10, 15 , sep=':', end= ' = ')
print(20)


# ---- Data Types -----
# Numeric Types
print(10)         # integer
print(1e309)    # float (infinity)
print(3.23)      # float
print(1.7e309)
print(5 + 2j)    # complex

# Text Types
print("Hello")   # string
print('A')       # character (string of length 1)
print(True)      # boolean and data types.
print(False)

print([1, 2, 3])        # list --> in c++/java: array
print((1, 2, 3))        # tuple
print({"name": "Eren", "age": 15})  # dictionary
print({1, 2, 3})       # set
print(None)            # NoneType

#type checking
print(type([1, 2, 3]))

# ----- Variables -----
# variables are used to store data values.
# In Python, you don't need to declare the type of a variable.
# static Vs dynamic typing
# static vs dynamic Binding
# stylish declaration of variables

name = "Mikasa Ackerman"
print(name)

#dynamic typing
age = 15
print(age)
# static typing
# int age = 15  [age: int = 15] # This will raise an error in Python as Python does not support static typing by default.

# dynamic binding
age = "Fifteen"
print(age)
age = 15 # re-binding
print(age)
# static binding
# int age = 15
# age = "Fifteen"  # This will raise an error in statically typed languages.

# variable naming rules
# 1. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
# 2. The rest of the variable name can contain letters, numbers (0-9), and underscores.
# 3. Variable names are case-sensitive (age, Age, and AGE are three different
#    variables).
# 4. Variable names cannot be a reserved keyword in Python (like print, if, else, etc.).
my_variable = 10
_myVariable = 20
myVariable2 = 30
# 2myVariable = 40  # This will raise an error
print(my_variable, _myVariable, myVariable2)

# ----- Multiple Assignment -----
x, y, z = 5, 10, 15
print(x, y, z)
a = b = c = 20
print(a, b, c)

# ----- Comments -----
# This is a single-line comment
"""
This is a multi-line comment
"""
'''This is another way to write multi-line comments'''
# Comments are used to explain code and make it more readable.
# They are ignored by the Python interpreter.
# Remember to use comments wisely to enhance code understanding!

# keywords & identifiers in python
# Keywords are reserved words in Python that have special meanings.
# Identifiers are names used to identify variables, functions, classes, etc.
# You cannot use keywords as identifiers.
# Example of keywords: if, else, while, for, def, return, etc.
# Example of identifiers: my_variable, calculate_sum, Person, etc.
# You can find the list of keywords in Python using the keyword module.
import keyword
print(keyword.kwlist)

# uset input() function to take user input
user_name = input("Enter your name: ")
print("Hello, " + user_name + "! Welcome to Python programming.")   
# static vs dynamic typing  
# static typing: variable types are known at compile time
# dynamic typing: variable types are known at runtime
# Python uses dynamic typing
age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.")

# Type Conversion
# implicit vs explicit type conversion
num1 = 10      # integer
num2 = 3.14    # float
# implicit type conversion
result = num1 + num2  # num1 is converted to float
print(result)
# explicit type conversion
# print(8 + '8')  # This will raise an error
print(8 + int('8'))  # Correct way

# Literals in Python
# Literals are the data values that are assigned to variables.
a = 10          # integer literal
# Different number systems
binary_num = 0b1010    # binary literal (10 in decimal)
octal_num = 0o12       # octal literal (10 in decimal)
hexadecimal_num = 0xA  # hexadecimal literal (10 in decimal)
print(binary_num, octal_num, hexadecimal_num)
# float literals
float_num1 = 3.14      # decimal float literal
float_num2 = 1e3       # scientific notation (1000.0) 10^3
print(float_num1, float_num2)
# complex literals
complex_num = 5 + 2j   # complex literal
print(complex_num.imag)
# string literals
string_literal = "Hello, Python!"
print(string_literal)
multline_string = """This is a
multi-line string literal."""
print(multline_string)
unicode = u"Hello, \u03A9"  # Unicode string literal
print(unicode)
raw_string = r"C:\Users\Name"  # Raw string literal
print(raw_string)

l = True + False  # boolean literals
print(l)
v = (True + 2) * 10
print(v)

# ===== End of Basics1 of Python =====