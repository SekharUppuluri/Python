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


