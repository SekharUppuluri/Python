# === Sets ===

# -- A set is an unordered collection of items. Every set element is unique (no duplicates) and must be immutable (cannot be changed).
# -- However, a set itself is mutable. We can add or remove items from it.
# -- Sets can also be used to perform mathematical set operations like union, intersection, symmetric difference, etc.

# Characteristics:
# - Unordered
# - Mutable
# - No Duplicates
# - Can't contain mutable data types

# Creating a set

# Empty set
s = set()
print(s)
print(type(s))

# 1D set
s1 = {1, 2, 3}
print(s1)

# 2D set (not allowed, as sets can't contain mutable elements like other sets)
# s2 = {1, 2, 3, {4, 5}}  #  TypeError
# print(s2)

# Heterogeneous set (can contain different immutable types)
s3 = {1, 'hello', 4.5, (1, 2, 3)}
print(s3)

# Using type conversion to create a set from a list
s4 = set([1, 2, 3])
print(s4)

# Duplicates are not allowed (automatically removed)
s5 = {1, 1, 2, 2, 3, 3}
print(s5)

# Sets can't contain mutable items (like lists)
# s6 = {1, 2, [3, 4]}  # TypeError
# print(s6)

s1 = {1,2,3}
s2 = {3,2,1}

print(s1 == s2)  # True, because sets are unordered

# Accessing Set Elements
# Sets are unordered, so we cannot access elements by index or slice.
# Attempting to do so will raise a TypeError.
s1 = {1, 2, 3, 4}
# s1[0:3]  # 'set' object is not subscriptable

# We can iterate through the set instead:
for item in s1:
    print(item)

# Editing Sets
# Sets are mutable, but we cannot edit individual elements by index.
# Attempting to do so will raise a TypeError.
s1 = {1, 2, 3, 4}
# s1[0] = 100  #  'set' object does not support item assignment

# To modify, we can remove and add elements:
s1.remove(1)
s1.add(100)
print(s1)

# Adding Elements
S = {1, 2, 3, 4}
# add (single element)
S.add(5)
print(S)
# update 
S.update([6, 7, 8])
print(S)