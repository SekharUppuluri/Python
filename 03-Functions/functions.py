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



