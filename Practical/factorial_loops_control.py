# === Calculate Factorial Using Loops and Control Statements ===

print("===== Factorial Calculation =====")
number  = int(input("Enter a number to calculate its factorial: "))

# ----- Factorial using FOR loop -----
factorial = 1

if number < 0:
    print("Factorial is not defined for negative numbers.")
else :
    for i in range(1, number + 1):
        if i == 0 :
            pass
        if i == 0 :
            continue
        factorial *= i
    else:
        print(f"\nThe factorial of {number} using for loop is {factorial}.")

# ----- Factorial using while loop -----
factorial = 1
count = number

if number >= 0 :
    while count > 0:
        if count == 0 :
            pass
        factorial *= count
        count -= 1
    else:
        print(f"The factorial of {number} using while loop is {factorial}.")

print("\n ----- End of Factorial Calculation ----- // Developed by アニン。")