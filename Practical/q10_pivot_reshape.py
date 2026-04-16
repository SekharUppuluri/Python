import pandas as pd

# Long-format data
df_long = pd.DataFrame({
    'employee': ['Anusha', 'Anusha', 'Celina', 'Celina', 'Charan', 'Charan'],
    'year': [2023, 2024, 2023, 2024, 2023, 2024],
    'salary': [55000, 58000, 60000, 63000, 52000, 54000]
})

print("Long Format Data:")
print(df_long)

# Long --> Wide (Pivoting)
df_wide = df_long.pivot(index='employee', columns='year', values='salary')

print("\nWide Format Data (Pivoted):")
print(df_wide)

# Wide --> Long (Unpivoting with melt())
df_long_again = df_wide.reset_index().melt(
    id_vars='employee',
    var_name='year',
    value_name='salary'
)

print("\nLong Format Data (Melted Back):")
print(df_long_again)