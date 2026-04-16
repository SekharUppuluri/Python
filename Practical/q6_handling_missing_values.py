import pandas as pd
import numpy as np

# Creating a DataFrame with missing values
data = {
    'Name': ['Arjun', 'Sita', 'Srinu', 'Ravi', 'Anu'],
    'Age': [25, np.nan, 30, 22, np.nan],
    'Salary': [50000, 60000, np.nan, 45000, 52000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Method 1: Filtering out missing values
filtered_df = df.dropna()
print("\nDataFrame after removing missing values:")
print(filtered_df)

# Method 2: Filling missing values 
filled_df = df.copy()
filled_df['Age'] = filled_df['Age'].fillna(filled_df['Age'].mean())
filled_df['Salary'] = filled_df['Salary'].fillna(filled_df['Salary'].mean())

print("\nDataFrame after filling missing values:")
print(filled_df)