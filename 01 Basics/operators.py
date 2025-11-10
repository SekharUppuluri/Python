# ===== Basics of Operators in Python =====

# Operators in Python
# Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Comparison Operators
print("\nComparison Operators:")
print("Equal: " , a == b)
print("Not Equal: ", a != b)
print("Greater Than: ", a > b)
print("Less Than: ", a < b)
print("Greater Than or Equal To: ", a >= b)
print("Less Than or Equal To: ", a <= b)

# Logical Operators
print("\nLogical Operators:")
x = True
y = False
print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)

# Assignment Operators
print("\nAssignment Operators:")
c = 5
print("Initial value of c:", c)
c += 2
print("After c += 2:", c)
c *= 3
print("After c *= 3:", c)
c -= 4
print("After c -= 4:", c)
c /= 2
print("After c /= 2:", c)

# Identity Operators
print("\nIdentity Operators:")
m = [1, 2, 3]
n = m
print("m is n:", m is n)
print("m is not n:", m is not n)

# Membership Operators
print("\nMembership Operators:")
lst = [1, 2, 3, 4, 5]
print("3 in lst:", 3 in lst)
print("6 not in lst:", 6 not in lst)
# Bitwise Operators
print("\nBitwise Operators:")
p = 5  # 0101 in binary
q = 3  # 0011 in binary
print("Bitwise AND:", p & q)   # 0001
print("Bitwise OR:", p | q)    # 0111
print("Bitwise XOR:", p ^ q)   # 0110
print("Bitwise NOT:", ~p)       # -0110
print("Left Shift:", p << 1)    # 1010
print("Right Shift:", p >> 1)   # 0010
# Operator Precedence
print("\nOperator Precedence:")
result = 10 + 3 * 2 ** 2
print("10 + 3 * 2 ** 2 =", result)  # 10 + 3 * 4 = 10 + 12 = 22
# Parentheses can change precedence
result = (10 + 3) * 2 ** 2
print("(10 + 3) * 2 ** 2 =", result)  # 13 * 4 = 52

# This concludes the basics of operators in Python.