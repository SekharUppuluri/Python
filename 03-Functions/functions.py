# ======= Functions =======
"""
    Functions are reusable blocks of code that perform a specific task.
    They help in organizing code, improving readability, and reducing redundancy.
""" 

def python_fun():
    print("This is a python function")
    return

# Calling the function
python_fun()

print(type.__doc__)  # Documentation for the type function
# docstring for user-defined function
def sample_function():
    """This is a sample function to demonstrate docstrings in Python."""
    pass
print(sample_function.__doc__)  # Accessing the docstring


# ----- Function Parameters and Arguments -----
"""
     ----- Parameters vs Arguments:
    - Parameters are the variables defined in the function definition.
    - Arguments are the actual values passed to the function when it is called.

    Types of Arguments:
    1. Positional Arguments: Arguments that need to be in the same order as the
         parameters in the function definition.
    2. Keyword Arguments: Arguments that are passed by explicitly specifying the
         parameter name and value.
    3. Default Arguments: Parameters that have a default value if no argument
            is provided during the function call.
    4. Variable-length Arguments: Allows passing a variable number of arguments
            using *args (non-keyword arguments) and **kwargs (keyword arguments).
"""

def add(A = 3, S = 2):
    return A + S

# positional arguments
print(add(5, 7)) 

# keyword arguments
print(add(S = 10, A = 4))

# default arguments
print(add())
print(add(10)) 

# variable-length arguments
# Using *args
def multiply(*args):  # or *numbers
    result = 1
    for num in args:
        result *= num
    return result
print(multiply(2, 3, 4))

# Using **kwargs
def display_info(**kwargs):  # or **data
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(name="Alice", age=30, city="New York")

""" Points to remember while using *args and **kwargs

     -> order of the arguments matter(normal -> *args -> **kwargs)
     -> The words “args” and “kwargs” are only a convention, you can use any name of your choice
"""
def sample_function(normal, *args, **kwargs):
    print("Normal Argument:", normal)
    print("*args:", args)
    print("**kwargs:", kwargs)

sample_function("normal_value", 1, 2, 3, key1="value1", key2="value2")

# ----- Return Statement -----
def square(num):
    return num * num  # If no return statement then it returns None by default
result = square(5) 
print("Square of 5 is:", result)


""" ----- How Functions are executed in memory? ------

When a function is called, a new block is created in memory for that function's execution. This block contains:
1. **Local Variables**: Variables defined within the function.
2. **Parameters**: Values passed to the function.
3. **Return Address**: Where to go back after the function finishes.
Once the function completes its execution, this block is removed from memory, and control returns to the point where the function was called.

"""
# Example to illustrate memory execution
def memory_example(x):
    y = x + 5
    return y
result = memory_example(10)
print("Result from memory_example:", result)

# ----- Variables Scope -----
"""
    - Local Scope: Variables defined within a function are local to that function.
    - Global Scope: Variables defined outside any function are global and can be accessed anywhere in the code.
    - Nonlocal Scope: Used in nested functions to refer to variables in the nearest enclosing scope that is not global.
"""
# Local Scope 
def local_scope():
    local_var = "I am local"
    print(local_var)
 
local_scope()
#print(local_var) # This will raise an error as local_var is not defined globally

# Global Scope
global_var = "I am global"
def global_scope():
    print(global_var)
global_scope()
print(global_var)  # Accessible here as well

# Nonlocal Scope
def outer_function():
    outer_var = "I am outer"
    def inner_function():
        nonlocal outer_var
        outer_var = "I am modified outer"
        print(outer_var)
    inner_function()
    print(outer_var)
outer_function()

# Note: Avoid using global variables excessively as they can make code harder to debug and maintain.

# ----- Nested Functions -----
def outer():
    print("This is the outer function")
    def inner():
        print("This is the inner function")
    inner()  # Calling inner function within outer function
outer()  # Calling outer function
# You can also return the inner function
def outer_return():
    print("Outer function called")
    def inner():
        print("Inner function called")
    return inner  # Returning the inner function without calling it
inner_function = outer_return()  # Call outer_return to get inner function
inner_function()  # Now call the returned inner function
# This allows for function factories and decorators

def f():
  def g():
    print('inside function g')
    f()
  g()
  print('inside function f')
f()  # Note: Be cautious with recursion to avoid infinite loops.


# ----- fUNCTIONS ARE FIRST-CLASS CITIZENS -----
"""
    In Python, functions are first-class citizens, meaning they can be:
    - Assigned to variables
    - Passed as arguments to other functions
    - Returned from other functions
    - Stored in data structures like lists, tuples, and dictionaries
"""
# # Assigning function to a variable
# def greet(name):
#     return f"Hello, {name}!"
# say_hello = greet
# print(say_hello("Eren"))
# # Passing function as an argument
# def call_function(func, value):
#     return func(value)
# result = call_function(greet, "Mikasa")
# print(result)
# # Returning function from another function
# def outer_function():
#     def inner_function(name):
#         return f"Hi, {name}!"
#     return inner_function
# new_greet = outer_function()
# print(new_greet("Eren"))
# # Storing functions in a list
# function_list = [greet, new_greet]
# for func in function_list:
#     print(func("Armin"))
# # Storing functions in a dictionary
# function_dict = {
#     'greet': greet,
#     'new_greet': new_greet
# }
# print(function_dict['greet']("Eren"))
# print(function_dict['new_greet']("Mikasa"))

# ----- BENEFITS OF FUNCTIONS -----
"""
    - Code Reusability: Write once, use multiple times.
    - Modularity: Break down complex problems into smaller, manageable functions.
    - Readability: Clear structure and organization of code.
    - Maintainability: Easier to update and fix bugs in isolated functions.
    - Testing: Functions can be tested independently for correctness.
"""

# Example demonstrating benefits
def calculate_area(radius):
    import math
    return math.pi * radius * radius
area1 = calculate_area(5)
area2 = calculate_area(10)
print("Area of circle with radius 5:", area1)
print("Area of circle with radius 10:", area2)
# This function can be reused for different radius values without rewriting the area calculation logic.

# ------ lambda Functions ------
"""
    - Lambda functions are small anonymous functions defined using the lambda keyword.
    - They can take any number of arguments but can only have one expression.
    - Syntax: lambda arguments: expression
    - Commonly used for short, throwaway functions, especially as arguments to higher-order functions like map(), filter(), and sorted().
"""
#  lambda function
square = lambda x: x * x
print("Square of 6 using lambda:", square(6))

# ------- Difference between lambda and regular functions -----
"""
    - Lambda functions are limited to a single expression and cannot contain statements or annotations.
    - Regular functions can have multiple expressions, statements, and annotations.
    - Lambda functions are syntactically restricted to a single line.
    - Regular functions can be more verbose and include documentation.
"""
#  regular function
def regular_square(x):
    return x * x
print("Square of 6 using regular function:", regular_square(6))
#  lambda function
lambda_square = lambda x: x * x
print("Square of 6 using lambda function:", lambda_square(6))

# Using lambda with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print("Squared numbers using map:", squared_numbers)

# Using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter:", even_numbers)

# Using lambda with sorted()
students = [('Eren', 25), ('Mikasa', 20), ('Armin', 23)]
sorted_students = sorted(students, key=lambda student: student[1])
print("Students sorted by age using lambda:", sorted_students)
# Note: For complex functions, it's better to use regular function definitions for clarity.

# using lambda with reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers using reduce:", product)
