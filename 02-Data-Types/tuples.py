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

# Accessing Items in a Tuple
# - Indexing
# - Slicing

# Example tuple
print("Tuple t3:", t3) 

# Indexing examples
print("First element (t3[0]):", t3[0])      
print("Last element (t3[-1]):", t3[-1])    

# Nested tuple access
print("Nested access (t5[-1][0]):", t5[-1][0]) 

# Slicing examples (adding for completeness)
print("Slice t3[1:3]:", t3[1:3])            
print("Slice t3[::-1]:", t3[::-1])


# Editing a Tuple

print("Original tuple t3:", t3)
t3[0] = 100 
# Tuples are immutable, just like strings


# Adding Items to a Tuple
print("Current tuple t3:", t3)
# Adding directly is not possible due to immutability

# Deleting a Tuple
print(t3)
del t3
print(t3)

t = (1,2,3,4,5)
print(t[-1:-4:-1])

# Operations on Tuples

# Concatenation using +
t1 = (1, 2, 3, 4)
t2 = (5, 6, 7, 8)
print("Concatenation (t1 + t2):", t1 + t2)

# Repetition using *
print("Repetition (t1 * 3):", t1 * 3)

# Membership testing
print("Membership (1 in t1):", 1 in t1)

# Iteration
print("Iteration over t1:")
for i in t1:
    print(i)

# Functions Applicable to Tuples
# len/sum/min/max/sorted
t = (1, 2, 3, 4)
print("Length of t:", len(t))
print("Sum of t:", sum(t))
print("Min of t:", min(t))
print("Max of t:", max(t))
print("Sorted t (reverse=True):", sorted(t, reverse=True))

# count
t = (1, 2, 3, 4, 5)
print("Count of 5 in t:", t.count(5))  
print("Count of 50 in t:", t.count(50))  

# index
print("Index of 5 in t:", t.index(5)) 
# print("Index of 50 in t:", t.index(50))  # This would raise ValueError since 50 not in t

# ===== Differences between Lists and Tuples =====

# Key Differences:
# - Syntax: Lists use [], tuples use ()
# - Mutability: Lists are mutable, tuples are immutable
# - Speed: Tuples are faster for iteration
# - Memory: Tuples use less memory
# - Built-in functionality: Lists have more methods
# - Error prone: Lists can be modified accidentally
# - Usability: Tuples for fixed data, lists for dynamic data

import time
import sys

# Speed Comparison
print("Speed Comparison:")
L = list(range(1000000))  # Reduced size for practicality
T = tuple(range(1000000))

start = time.time()
for i in L:
    i * 5
print('List time:', time.time() - start)

start = time.time()
for i in T:
    i * 5
print('Tuple time:', time.time() - start)

# Memory Comparison
print("\nMemory Comparison:")
L = list(range(1000))
T = tuple(range(1000))

print('List size:', sys.getsizeof(L))
print('Tuple size:', sys.getsizeof(T))

# Mutability Example with Lists
print("\nMutability Example with Lists:")
a = [1, 2, 3]
b = a

a.append(4)
print("a:", a)
print("b:", b)  # b is affected because lists are mutable

# Immutability Example with Tuples
print("\nImmutability Example with Tuples:")
a = (1, 2, 3)
b = a

a = a + (4,)  # Creates a new tuple
print("a:", a)
print("b:", b)  # b remains unchanged because tuples are immutable

# ===== Why Use Tuples? =====
# - Simple syntax
# - Tuple unpacking

# Basic tuple unpacking
a, b, c = (1, 2, 3)
print(a, b, c)

# Unpacking with fewer variables (will raise ValueError due to mismatch)
# a, b = (1, 2, 3)  # Commented out to avoid error
# print(a, b)

# Swapping values using tuple unpacking
a = 1
b = 2
a, b = b, a
print(a, b)

# Extended unpacking with *others
a, b, *others = (1, 2, 3, 4)
print(a, b)
print(others)

# ===== Zipping Tuples =====
a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
zipped = tuple(zip(a, b))
print(zipped)