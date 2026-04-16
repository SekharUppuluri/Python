import pandas as pd 

# Define sample employee data
data = {
    'Name': ['Siva Ganesh', 'Sai Karthik', 'Priya', 'Poorna(Reddy)', 'DP (Durga Prasad)', 'Sunkara Swamy'],
    'Department': ['IT', 'Finance', 'IT', 'Marketing', 'IT', 'HR'],
    'Salary': [70000, 75000, 90000, 65000, 72000, 60000]
}

# Create DataFrame from the data dictionary
df = pd.DataFrame(data)

# Display the original DataFrame
print("\nOriginal DataFrame:")
print(df)

# Sort DataFrame by Salary in ascending order (lowest to highest)
df_asc = df.sort_values(by='Salary', ascending=True)
print("\nDataFrame Sorted by Salary (Ascending):")
print(df_asc)

# Sort DataFrame by Salary in descending order (highest to lowest)
df_desc = df.sort_values(by='Salary', ascending=False)
print("\nDataFrame Sorted by Salary (Descending):")
print(df_desc)

# Add a new column with salary rankings (1 = highest salary)
df['Salary Rank'] = df['Salary'].rank(ascending=False)
print("\nDataFrame with Salary Rank:")
print(df)
