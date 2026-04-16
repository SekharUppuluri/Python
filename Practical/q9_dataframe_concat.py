import pandas as pd

# Create small DataFrames
df1 = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4]
})

df2 = pd.DataFrame({
    'A': [5, 6],
    'B': [7, 8]
})

df3 = pd.DataFrame({
    'A': ['x', 'y'],
    'B': ['p', 'q']
})

print("DataFrame 1:")
print(df1)

print("\nDataFrame 2:")
print(df2)

print("\nDataFrame 3:")
print(df3)

# Concatenate along rows (axis=0)
# Stacks df1 and df2 vertically
concat_rows = pd.concat([df1, df2], axis=0)

print("\nConcatenated along Rows (axis=0):")
print(concat_rows)

# Concatenate along columns (axis=1)
# Combines df1 and df3 side by side
concat_cols = pd.concat([df1, df3], axis=1)

print("\nConcatenated along Columns (axis=1):")
print(concat_cols)