# ## 1. Lists

# - What are Lists?
# - Lists Vs Arrays
# - Characteristics of a List
# - How to create a list
# - Access items from a List
# - Editing items in a List
# - Deleting items from a List
# - Operations on Lists
# - Functions on Lists
# - List Comprehensions
# - Nested Lists
# - Conclusion

# ===== Lists =====
# what are Lists?
# Lists are ordered collections of items that can hold multiple data types.
# They are mutable, meaning their contents can be changed after creation.

# - Lists Vs Arrays
# Lists can hold items of different data types, while arrays typically hold items of the same data type.
# Lists are more flexible and easier to use for general purposes, while arrays are more efficient for numerical computations.
# - Fixed Vs Dynamic Size
# - Convenience -> Heterogeneous
# - Speed of Execution
# - Memory

from git import List


L = [1,2,3]

print("ID of L:", id(L))
print("ID of L[0]:", id(L[0]))
print("ID of L[1]:", id(L[1]))
print("ID of L[2]:", id(L[2]))
print("ID of 1:", id(1))
print("ID of 2:", id(2))
print("ID of 3:", id(3))

# Characteristics of a List:
# - Ordered: Items have a defined order, and that order will not change unless you explicitly do so.
# - Mutable: You can change, add, and remove items after the list has been created.
# - Allows Duplicates: Since lists are indexed, they can have items with the same value.
# - Heterogeneous: Lists can contain items of different data types.
# - Dynamic: Lists can grow and shrink in size as needed.
# - Can be nested: Lists can contain other lists.
# - Items can be accessed: Elements can be retrieved by index.
# - Can contain any kind of objects in Python.

l1 = [1, 2, 3]
l2 = [3, 2, 1]
print("l1 == l2:", l1 == l2)  # False, because order matters in lists

# How to create a list

# Empty list
print([])

# 1D Homogeneous list (same data type)
print("1D :", [1, 2, 3, 4, 5])

# 2D list (nested list)
print("2D :", [1, 2, 3, [4, 5]])

# 3D list (deeply nested)
print("3D :", [[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Heterogeneous list (mixed data types)
print([1, True, 5.6, 5+6j, 'Hello'])

# Using type conversion to create a list from a string
print(list('hello'))

# Access items from a List
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

print("First item:", my_list[0])        # Accessing first item
print("Second item:", my_list[1])       
print("Last item:", my_list[-1])        # Accessing last item
print("Second last item:", my_list[-2])
print("Items from index 1 to 3:", my_list[1:4]) # Slicing 
print("Every second item:", my_list[::2]) # Slicing with step
print("Reversed list:", my_list[::-1])  
print("Nested item:", my_list[2][1])    

# Adding items to a List
my_list.append('fig')                    # Append item at the end
print("After append:", my_list)
my_list.insert(1, 'blueberry')          # Insert item at index 1
print("After insert:", my_list)
my_list.extend(['grape', 'honeydew'])   # Extend list with another list
print("After extend:", my_list)

# Editing items in a List
my_list[0] = 'apricot'                  # Indexing
print("After editing first item:", my_list)
my_list[1:3] = ['blackberry', 'cantaloupe']  # Slicing
print("After editing multiple items:", my_list)

# Deleting items from a List
my_list.remove('date')                   # Remove by value
print("After remove:", my_list)
popped_item = my_list.pop(2)            # Remove by index
print("After pop:", my_list)
print("Popped item:", popped_item)
del my_list[0]                          # Delete by index
print("After del:", my_list)
my_list.clear()                         # Clear the entire list
print("After clear:", my_list)

# Operations on Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2                 # Concatenation
print("Concatenated list:", combined)
repeated = list1 * 3                     # Repetition
print("Repeated list:", repeated)

# Check membership
print("Is 2 in list1?", 2 in list1)
print("Is 5 not in list1?", 5 not in list1)

# Iterate through a list
for item in list1:
    print("Item:", item)

# Functions on Lists
numbers = [10, 20, 30, 40, 50]

print("Length of numbers:", len(numbers))
print("Max of numbers:", max(numbers))
print("Min of numbers:", min(numbers))
print("Sum of numbers:", sum(numbers))
print("Sorted numbers:", sorted(numbers, reverse=True))

print("Index of 30:", numbers.index(30))
print("Count of 20:", numbers.count(20))

# sort vs sorted
# sorted() returns a new sorted list without modifying the original
original = [3, 1, 4, 1, 5]
print("Original list:", original)
sorted_copy = sorted(original)
print("After sorted(): original =", original, ", sorted_copy =", sorted_copy)
# sort() modifies the list in place and returns None
original.sort()
print("After sort(): original =", original)

numbers.reverse()   # permanently reverses the list
print("Numbers after reverse:", numbers)

print("ID of numbers before copy:", id(numbers))
copied_numbers = numbers.copy()  # Shallow copy
print("ID of numbers after copy:", id(numbers))
print("ID of copied_numbers:", id(copied_numbers))
print("Copy of numbers:", copied_numbers)


# List Comprehensions

# List Comprehension provides a concise way of creating lists.

# newlist = [expression for item in iterable if condition == True]
# Advantages of List Comprehension
# - More time-efficient and space-efficient than loops.
# - Require fewer lines of code.
# - Transforms iterative statement into a formula.

L = []

for i in range(1, 11):
    L.append(i)

print(L)
L = [i for i in range(1, 11)]
print(L)

# scalar multiplication on a vector
v = [2, 3, 4]
s = -3
# [-6, -9, -12]

print([s * i for i in v])
# Add squares
L = [1, 2, 3, 4, 5]

print([i**2 for i in L])
# Print all numbers divisible by 5 in the range of 1 to 50

print([i for i in range(1, 51) if i % 5 == 0])
# find languages which start with letter p
languages = ['java', 'python', 'php', 'c', 'javascript']

print([language for language in languages if language.startswith('p')])
# Nested if with List Comprehension
basket = ['apple', 'guava', 'cherry', 'banana']
my_fruits = ['apple', 'kiwi', 'grapes', 'banana']

# add new list from my_fruits and items if the fruit exists in basket and also starts with 'a'

print([fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')])
# Print a (3,3) matrix using list comprehension -> Nested List comprehension
print([[i * j for i in range(1, 4)] for j in range(1, 4)])
# cartesian products -> List comprehension on 2 lists together
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

print([i * j for i in L1 for j in L2])


## 2 ways to traverse a list

# - itemwise
# - indexwise
for item in languages:
    print("Language:", item)
for index in range(0, len(languages)):
    print("Language at index", index, "is", languages[index])

