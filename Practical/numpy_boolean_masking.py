import numpy as np

# Generate a NumPy Array with random integers
arr = np.random.randint(10, 101, size=10)

print("Original Array : ")
print(arr)

# target value
target = 50

# Apply conditional logic using indexing
# Set values greater than 50 to 100
arr_modified = arr.copy()
arr_modified[arr_modified > target] = 100

print("\nArray after applying Condition (values > 50 set to 100) : ")
print(arr_modified)

arr_modified2 = arr.copy()
# Set values less than or equal to 50 to 0
arr_modified2[arr_modified2 <= target] = 0

print("\nArray after applying Condition (values <= 50 set to 0) : ")
print(arr_modified2)


# Conditional replacement using np.where()
arr_where = np.where(arr > target, 100, arr)

print("\nArray after applying np.where() (values > 50 set to 100) : ")
print(arr_where)

arr_where2 = np.where(arr <= target, 0, arr)
print("\nArray after applying np.where() (values <= 50 set to 0) : ")
print(arr_where2)

# Multiple conditions using np.where()
arr_where_multiple = np.where(arr > target, 100, 0)
print("\nArray with multiple conditions : ")
print(arr_where_multiple)