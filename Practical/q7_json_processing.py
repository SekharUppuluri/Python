import pandas as pd

# Step 1: Load data from JSON file
df = pd.read_json("student.json")

print("Original Data Frame:")
print(df)

# Step 2: Process the DataFrame (Example)
df["processed_flag"] = True

# Step 3: Save the processed DataFrame back to JSON
df.to_json("processed_studentdata.json", orient="records", indent=4)

print("\nProcessed data saved to processed_studentdata.json")