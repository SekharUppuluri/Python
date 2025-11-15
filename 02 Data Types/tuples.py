# ===== Tuples =====
# Tuples

# A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.
# In short, a tuple is an immutable list. A tuple can not be changed in any way once it is created.

# Characterstics
# - Ordered
# - Unchangeble
# - Allows duplicate

# Creating a tuple

# Empty tuple
t1 = ()
print(t1)

# Tuple with a single item (note the comma)
t2 = ('hello',)
print(t2)
print(type(t2))

# Homogeneous tuple (all elements of the same type)
t3 = (1, 2, 3, 4)
print(t3)

# Heterogeneous tuple (elements of different types)
t4 = (1, 2.5, True, [1, 2, 3])
print(t4)

# Nested tuple
t5 = (1, 2, 3, (4, 5))
print(t5)

# Using type conversion to create a tuple from a string
t6 = tuple('hello')
print(t6)