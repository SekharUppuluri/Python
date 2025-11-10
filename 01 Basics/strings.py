# ===== Strings =====
# Strings are sequences of characters enclosed in single or double quotes.
# Strings are immutable, meaning they cannot be changed after creation.

# Creating strings
name = "Eren Yeager"
greeting = 'Hello, ' + name + '!'
print(greeting)
# Multi-line strings
multi_line = """This is a
multi-line string.
It can span multiple lines."""
print(multi_line)

# String indexing and slicing
first_char = name[0]
print("First character:", first_char)
print("Substring:", name[0:4])
print("Last character:", name[-1])
print("Every second character:", name[::2])
print("Reversed string:", name[::-1])
print(name[2:10:2])

# String methods
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Count of 'e':", name.count('e'))
print("Replaced name:", name.replace("Eren", "Armin"))
print("Split name:", name.split(" "))
print("Is digit:", "123".isdigit())
print("Is alpha:", "Eren".isalpha())
print("Length of name:", len(name))

# String formatting
age = 15
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)
f_string = f"My name is {name} and I am {age} years old."
print(f_string)

# Escape sequences
print("This is a line break:\nSee?")
print("This is a tab:\tSee?")
print("This is a backslash: \\")
print("He said, \"Hello!\"")
