import numpy as np
import pandas as pd

# Setting seed for reproducibility
np.random.seed(2)

# Creating a DataFrame with random numbers (5 rows and 3 columns)
data = np.random.randn(5, 3)
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

print("DataFrame with Random Numbers:")
print(df)

# Computing descriptive statistics
mean_values = df.mean()
median_values = df.median()
std_values = df.std()
min_values = df.min()
max_values = df.max()

# Displaying the statistics
print("\nMean:")
print(mean_values)

print("\nMedian:")
print(median_values)

print("\nStandard Deviation:")
print(std_values)

print("\nMinimum Values:")
print(min_values)

print("\nMaximum Values:")
print(max_values)
