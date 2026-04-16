import pandas as pd
import numpy as np

# Create a DataFrame with duplicates and missing values
df = pd.DataFrame({
    'name': ['Amit', 'Dileep', 'Charan', 'Anusha', 'Srithi'],
    'department': ['HR', 'IT', 'Finance', 'HR', None],
    'salary': [50000, 60000, np.nan, 50000, 60000]
})

print("Original DataFrame:")
print(df)

# 1. Remove duplicate rows
df_no_duplicates = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df_no_duplicates)

# 2. Replace specific values
# Example: Replace 'HR' with 'Human Resources'
df_replaced = df_no_duplicates.replace({'department': {'HR': 'Human Resources'}})

print("\nAfter Replacing Specific Values:")
print(df_replaced)

# 3. Handle Missing Data
# Fill missing salary with mean, missing department with a placeholder
df_cleaned = df_replaced.copy()
df_cleaned['salary'] = df_cleaned['salary'].fillna(df_cleaned['salary'].mean())
df_cleaned['department'] = df_cleaned['department'].fillna('Unknown')

print("\nAfter Handling Missing Data:")
print(df_cleaned)