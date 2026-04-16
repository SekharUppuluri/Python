import pandas as pd

# Step 1: Read data from an Excel file
# Assumes the file has a default sheet or a sheet named "Sheet1"
df = pd.read_excel("Employee_data.xlsx")

print("Original Data:")
print(df.head())

# Step 2: Basic Data Cleaning

# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing values (example: fill missing salaries with mean)
if "Salary" in df.columns:
    df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Strip whitespace from string columns
str_cols = df.select_dtypes(include="object").columns
df[str_cols] = df[str_cols].apply(lambda col: col.str.strip())

# Drop rows where all values are missing
df = df.dropna(how="all")

print("\nCleaned Data:")
print(df.head())

# Step 3: Save cleaned data to HDF5 format
df.to_hdf("Cleaned_data.h5", key="employees", mode='w')

print("\nCleaned data saved to Cleaned_data.h5")

# Read the HDF5 file
df = pd.read_hdf("Cleaned_data.h5")

# Display data from HDF5 file
print("\nData read from HDF5 file:")
print(df)