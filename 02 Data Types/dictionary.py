# === Dictionary ===

# Dictionary in Python is a collection of keys values, used to store data values like a map, which, unlike other data types which hold only a single value as an element.

# In some languages it is known as map or assosiative arrays.

# dict = { 'name' : 'nitish' , 'age' : 33 , 'gender' : 'male' }

# --- Characteristics: ---

# - Mutable
# - Indexing has no meaning
# - keys can't be duplicated
# - keys can't be mutable items
# - values can be duplicated

# Creating a Dictionary
# 1. Empty dictionary
d = {}
print("Empty dictionary:", d)

# 2. 1D dictionary with string keys
d1 = {'name': 'Reddy', 'gender': 'female'}
print("1D dictionary:", d1)

# 3. Dictionary with mixed keys (tuple and string)
d2 = {(1, 2, 3): 1, 'hello': 'world'}
print("Dictionary with mixed keys:", d2)

# 4. 2D dictionary (nested, like JSON)
s = {
    'name': 'bob',
    'college': 'mit',
    'sem': 4,
    'subjects': {
        'dsa': 50,
        'maths': 67,
        'english': 34
    }
}
print("2D dictionary (nested):", s)

# 5. Creating dictionary using dict() function with a list of tuples
d4 = dict([('name', 'charlie'), ('age', 32), (3, 3)])
print("Dictionary from list of tuples:", d4)

# 6. Duplicate keys (last one wins)
d5 = {'name': 'Divya', 'name': 'Sree'}
print("Dictionary with duplicate keys:", d5)

# 7. Using immutable items as keys (tuples are allowed, lists are not)
d6 = {'name': 'Reddy', (1, 2, 3): 2}
print("Dictionary with tuple as key:", d6)

# Accessing Dictionary Elements
my_dict = {'name': 'Jack', 'age': 26}
# Using []
print("Accessing 'age' with []:", my_dict['age'])
# Using get
print("Accessing 'age' with get:", my_dict.get('age'))

# Accessing nested dictionary
print("Accessing nested 'maths':", s['subjects']['maths'])


# Adding key-value pairs to a dictionary

# Adding to a simple dictionary
d4['gender'] = 'male'
print("After adding 'gender':", d4)

d4['weight'] = 72
print("After adding 'weight':", d4)

# Adding to a nested dictionary
s['subjects']['ds'] = 75
print("After adding 'ds' to nested dict:", s)


# Removing key-value pairs from a dictionary

# Example dictionary
d = {'name': 'nitish', 'age': 32, 3: 3, 'gender': 'male', 'weight': 72}

# Using pop() to remove a specific key-value pair
d.pop(3)
print("After pop(3):", d)

# Using popitem() to remove the last inserted key-value pair
d.popitem()
print("After popitem():", d)

# Using del to remove a specific key-value pair
del d['name']
print("After del d['name']:", d)

# Using clear() to remove all key-value pairs
d.clear()
print("After clear():", d)

# Removing from a nested dictionary
del s['subjects']['maths']
print("After deleting 'maths' from nested dict:", s)

# Editing key-value pairs in a dictionary
s['subjects']['dsa'] = 80
s['subjects']['english'] = 40
print("After editing nested dict:", s)


# ----- Dictionary Operations -----

# Membership: Check if a key exists in the dictionary
print("Dictionary s:", s)
print("'name' in s:", 'name' in s)

# Iteration: Loop through keys and access values
d = {'name': 'nitish', 'gender': 'male', 'age': 33}
for key in d:
    print(f"Key: {key}, Value: {d[key]}")


# ----- Dictionary Methods/Functions -----

# len/sorted
print("Length of d:", len(d))
print("Dictionary d:", d)
print("Sorted keys in reverse:", sorted(d, reverse=True))
print("Max key:", max(d))
print("Min key:", min(d))
print("Sum of keys (if numeric):", sum(d.keys()))  # only works if keys are numeric

# items/keys/values
print("Dictionary d:", d)
print("Items:", d.items())
print("Keys:", d.keys())
print("Values:", d.values())

# copy
d_copy = d.copy()
print("Copied dictionary:", d_copy)

# update
d1 = {1: 2, 3: 4, 4: 5}
d2 = {4: 7, 6: 8}
d1.update(d2)
print("Updated d1:", d1)

