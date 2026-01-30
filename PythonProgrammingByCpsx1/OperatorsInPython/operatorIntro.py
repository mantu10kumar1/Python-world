# Introduction to Operators in Python
# Operators are special symbols in Python that carry out arithmetic or logical computation.
# The value that the operator operates on is called the operand.
# Here are some common types of operators with output and definition in Python:

# List of Operators
# 1. Arithmetic Operators: +, -, *, /, %, **, //
# 2. Comparison Operators: ==, !=, >, <, >=, <=
# 3. Logical Operators: and, or, not
# 4. Assignment Operators: =, +=, -=, *=, /=, %=, **=, //=
# 5. Bitwise Operators: &, |, ^, ~, <<, >>, >>
# 6. Membership Operators: in, not in 
# 7. Identity Operators: is, is not
# 8. Power Operators: **, pow()
#------------------------------------------------------------------------

# Examples of Operators in Python

# 1. Arithmetic Operators
# Definition: Used to perform mathematical operations.

a = 10  
b = 3
print("Arithmetic Operators:")
print("Addition:", a + b)          # Output: 13
print("Subtraction:", a - b)       # Output: 7
print("Multiplication:", a * b)    # Output: 30
print("Division:", a / b)          # Output: 3.3333...
print("Modulus:", a % b)           # Output: 1
print("Exponentiation:", a ** b)   # Output: 1000
print("Floor Division:", a // b)    # Output: 3

print()
# 2. Comparison Operators   
# Relational operators are another term for comparison operators.
# Definition: Used to compare two values.

print("Comparison Operators:")
print("Equal to:", a == b)         # Output: False
print("Not equal to:", a != b)     # Output: True
print("Greater than:", a > b)      # Output: True
print("Less than:", a < b)         # Output: False
print("Greater than or equal to:", a >= b)  # Output: True
print("Less than or equal to:", a <= b)     # Output: False
print()

# 3. Logical Operators
# Definition: Used to combine conditional statements.
x = True
y = False
print("Logical Operators:")
print("AND:", x and y)             # Output: False
print("OR:", x or y)               # Output: True
print("NOT:", not x)               # Output: False
print()

# 4. Assignment Operators
# Definition: Used to assign values to variables.
c = 5
print("Assignment Operators:")
print("Initial value:", c)         # Output: 5
c += 2
print("After += 2:", c)            # Output: 7
c *= 3
print("After *= 3:", c)            # Output: 21
c -= 4
print("After -= 4:", c)            # Output: 17
c /= 2
print("After /= 2:", c)            # Output: 8.5
print()

# 5. Bitwise Operators
# Definition: Used to perform bit-level operations on integers.

p = 5      # Binary: 0101
q = 3      # Binary: 0011
print("Bitwise Operators:")
print("AND:", p & q)               # Output: 1 (Binary: 0001)
print("OR:", p | q)                # Output: 7 (Binary: 0111)
print("XOR:", p ^ q)               # Output: 6 (Binary: 0110)
print("NOT p:", ~p)                # Output: -6 (Binary: ...1010)
print("Left Shift p by 1:", p << 1) # Output: 10 (Binary: 1010)
print("Right Shift p by 1:", p >> 1) # Output: 2 (Binary: 0010)
print()

# 6. Membership Operators
# Definition: Used to test if a sequence contains a certain value.

my_list = [1, 2, 3, 4, 5]
print("Membership Operators:")
print("Is 3 in my_list?", 3 in my_list)         # Output: True
print("Is 6 not in my_list?", 6 not in my_list) # Output: True
print("D" in "Delhi")                           # Output: True
print()

# 7. Identity Operators
# Definition: Used to compare the memory locations of two objects.

m = [1, 2, 3]
n = m
o = [1, 2, 3]
print("Identity Operators:")
print("m is n:", m is n)               # Output: True
print("m is o:", m is o)               # Output: False  
print("m is not o:", m is not o)       # Output: True
print()

# Power operators in Python
# Definition: Used to perform exponentiation.
print("Power Operators:")
print("2 raised to the power 3 using **:", 2 ** 3)  # Output: 8
print("2 raised to the power 3 using pow():", pow(2, 3))  # Output: 8   

# This code provides a comprehensive introduction to various operators in Python along with examples and outputs.
# You can run this code in a Python environment to see the results for each operator type.


# WAP to calculate sum of digits of a 3 digit number

number = int(input("Enter a number : "))
a = number % 10
number = number // 10
b = number % 10
number = number // 10
c = number % 10 
sum = a + b + c
print("Sum of digits : " , sum)

