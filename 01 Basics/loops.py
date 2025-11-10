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