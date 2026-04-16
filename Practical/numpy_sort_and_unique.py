import numpy as np

# Create a numpy array with duplicate elements
arr = np.array([5, 2, 8, 5, 3, 2, 9, 8, 1, 5, 3])

print("Original Array:")
print(arr)

# Sort the array in ascending order
sorted_arr = np.sort(arr)
print("\nSorted Array:")
print(sorted_arr)

# Get unique elements from the array
unique_elements = np.unique(arr)
print("\nUnique Elements:")
print(unique_elements)
