# === Conditionals ===
# if, elif, and else statements allow you to control the flow of your program
# based on certain conditions.
# if statement
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# elif statement
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# Nested if statement
num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")

# Ternary operator (conditional expression)
is_even = "Even" if num % 2 == 0 else "Odd"
print(f"The number {num} is {is_even}.")