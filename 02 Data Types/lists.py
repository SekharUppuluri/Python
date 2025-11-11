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
