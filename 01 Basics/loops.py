# === Loops ===
# Loops are used to execute a block of code repeatedly.

# For loop
print("For loop:")
for i in range(5):
    print("Iteration:", i)

# While loop
print("\nWhile loop:")
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Nested loops
print("\nNested loops:")
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# Loop control statements
print("\nLoop control statements:")
print("\nUsing continue:")
for i in range(5):
    if i == 2:
        continue  # Skip the rest of the loop when i is 2
    print("Iteration:", i)

print("\nUsing break:")
for i in range(5):
    if i == 2:
        break  # Exit the loop when i is 2
    print("Iteration:", i)