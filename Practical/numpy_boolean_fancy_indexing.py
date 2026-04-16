import numpy as np

# Creating a NumPy array of random integers between 1 and 100
arr1 = np.random.randint(1, 101, size=10)

print("Original Array:")
print(arr1)

# Boolean Indexing
boolean_selected = arr1[arr1 > 50]
print("\nElements greater than 50 (Boolean Indexing):")
print(boolean_selected)

even_numbers = arr1[(arr1 % 2 == 0) & (arr1 > 30)]
print("\nEven numbers greater than 30:")
print(even_numbers)

# Fancy Indexing
indices = [1, 3, 5, 7]
fancy_selected = arr1[indices]
print("\nElements at indices [1, 3, 5, 7] (Fancy Indexing):")
print(fancy_selected)