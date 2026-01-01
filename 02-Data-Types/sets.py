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

# Deleting Elements

# del (not applicable for sets, as sets don't support indexing)
s = {1, 2, 3, 4, 5}
# del s[0]  # TypeError: 'set' object doesn't support item deletion by index

# discard (removes element if present, no error if not)
s.discard(50)
print(s)  # {1, 2, 3, 4, 5} (unchanged, since 50 not in set)

# remove (removes element if present, raises KeyError if not)
# s.remove(50)  # KeyError if 50 not in set

# pop (removes and returns an arbitrary element)
popped = s.pop()
print(f"Popped: {popped}")
print(s)

# clear (removes all elements)
s.clear()
print(s)  # set()


# Set Operations

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s1 | s2
# Union(|)
# Intersection(&)
s1 & s2
# Difference(-)
s1 - s2
s2 - s1
# Symmetric Difference(^)
s1 ^ s2
# Membership Test
1 not in s1
# Iteration
for i in s1:
  print(i)


# Set Functions
# len/sum/min/max/sorted
s = {3,1,4,5,2,7}
len(s)
sum(s)
min(s)
max(s)
sorted(s,reverse=True)

# union/update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

# s1 | s2
s1.union(s1)

s1.update(s2)
print(s1)
print(s2)

# intersection/intersection_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1.intersection(s2)

s1.intersection_update(s2)
print(s1)
print(s2)

# difference/difference_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1.difference(s2)

s1.difference_update(s2)
print(s1)
print(s2)


# symmetric_difference/symmetric_difference_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1.symmetric_difference(s2)

s1.symmetric_difference_update(s2)
print(s1)
print(s2)

# isdisjoint/issubset/issuperset
s1 = {1,2,3,4}
s2 = {7,8,5,6}

s1.isdisjoint(s2)


s1 = {1,2,3,4,5}
s2 = {3,4,5}

s1.issuperset(s2)


# copy
s1 = {1,2,3}
s2 = s1.copy()

print(s1)
print(s2)

# Frozenset
# Frozen set is just an immutable version of a Python set object.
# create frozenset
fs1 = frozenset([1,2,3])
fs2 = frozenset([3,4,5])

fs1 | fs2

# what works and what does not
# works -> all read functions
# does't work -> write operations
# When to use
# 2D sets
fs = frozenset([1,2,frozenset([3,4])])
fs


# Set Comprehension
{i**2 for i in range(1,11) if i>5}
