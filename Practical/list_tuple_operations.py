# === Demonstration of List and Tuple Operations ===

print("===== List and Tuple Operations =====")

print("\n----- List Operations -----")
grocery_list = ["rice", "milk", "eggs", "bread", "butter"]
print(f"Original grocery list: {grocery_list}")

# Accessing items
first_item = grocery_list[0]
print(f"First item: {first_item}")

# Adding an item
grocery_list.append("cheese")
print(f"After adding 'cheese': {grocery_list}")

# Removing an item
grocery_list.remove("milk")
print(f"After removing 'milk': {grocery_list}")

# Sorting the list
grocery_list.sort()
print(f"After sorting: {grocery_list}")

# Reversing the list
grocery_list.reverse()
print(f"After reversing: {grocery_list}")

# ----- Tuple Operations -----
print("\n----- Tuple Operations -----")
colors_tuple = ("red", "blue", "green", "yellow", "purple")

# Accessing items
first_color = colors_tuple[0]
print(f"First color: {first_color}")

# Slicing the tuple
sliced_colors = colors_tuple[1:4]
print(f"Sliced colors (1:4): {sliced_colors}")

# unpacking the tuple
(c1, c2, c3, c4, c5) = colors_tuple
print("\nUnpacked values:")
print(f"Color 1: {c1}")
print(f"Color 2: {c2}")
print(f"Color 3: {c3}")
print(f"Color 4: {c4}")
print(f"Color 5: {c5}")

print("\n ----- End of List and Tuple Operations ----- // Developed by アニン。")
