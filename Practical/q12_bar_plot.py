import pandas as pd
import matplotlib.pyplot as plt


# Sample dataset
df = pd.DataFrame({
    "department": ["HR", "IT", "Finance", "Marketing"],
    "employees": [12, 25, 18, 15]
})

print(df)

# Create a bar plot
plt.figure(figsize=(8, 5))

# Bar plot with custom colors
df.plot(
    kind="bar",
    x="department",
    y="employees",
    color=["skyblue", "orange", "green", "purple"],
    legend=False
)

# Label axes and title
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.title("Employee Count by Department")

# Rotate x-labels for readability
plt.xticks(rotation=0)

# Tight layout for clean spacing
plt.tight_layout()

# Save the plot as an image file
plt.savefig("department_employee_count.png", dpi=300)

# Show the plot
plt.show()