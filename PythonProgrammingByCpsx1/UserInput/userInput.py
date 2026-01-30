# Input() function in Python
# The input() function is used to take input from the user in Python. It reads a line from the input (usually from the user),
#  converts it into a string, and returns it.
# Syntax of input() function
# input(prompt)
# Here, prompt is an optional string that is displayed to the user before taking input.
# Example 1: Taking string input from the user
# name = input("Enter your name: ")
# print("Hello, " + name + "!")

# WAP to take two numbers as input from the user and print their sum
# Steps to follow: 

num1 = input("Enter first number : ")
num2 = input("Enter second number : ")
print("Type of num1 is : " , type(num1))
print("Type of num2 is : " , type(num2))

sum = num1 + num2 
print("The sum of " + num1 + " and " + num2 + " is : " + sum) 

# Type Conversion
# what is Type Conversion?
# Type conversion is the process of converting a value from one data type to another.
# Types of Type Conversion
# 1. Implicit Type Conversion 
# 2. Explicit Type Conversion
# Implicit Type Conversion
# In implicit type conversion, Python automatically converts one data type to another without any user intervention.
# Example of Implicit Type Conversion
a = 5       # integer
b = 2.5     # float
c = a + b   # implicit conversion of 'a' to float
print("The value of c is : " , c)
print("Type of c is : " , type(c))

# Implict type conversion not working always
x = "10"    # string
y = 5       # integer
# z = x + y  # This will raise a TypeError
# print("The value of z is : " , z)
# To perform the addition, we need to explicitly convert the string to an integer
z = int(x) + y  # explicit conversion of 'x' to integer
print("The value of z is : " , z)  # 15
print("Type of z is : " , type(z))  # integer



# Explicit Type Conversion
# In explicit type conversion, the user manually converts one data type to another using built-in functions
# Example of Explicit Type Conversion
num1 = input("Enter first number : ")
num2 = input("Enter second number : ")
# Converting string input to integer
num1 = int(num1)
num2 = int(num2)
sum = num1 + num2
print("The sum of " , num1 , " and " , num2 , " is : " , sum)
print("Type of num1 after conversion is : " , type(num1))
print("Type of num2 after conversion is : " , type(num2))

# You can also convert to other data types like float, str, etc.
# Converting string input to float
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
sum = num1 + num2
print("The sum of " , num1 , " and " , num2 , " is : " , sum)
print("Type of num1 after conversion is : " , type(num1))
print("Type of num2 after conversion is : " , type(num2))

# Note: Always ensure that the input can be converted to the desired data type to avoid runtime errors.

# Summary of above code
# 1. The input() function is used to take input from the user in Python.
# 2. Type conversion is the process of converting a value from one data type to another.
# 3. Implicit type conversion is done automatically by Python, while explicit type conversion is done manually by the user.
# 4. Use int(), float(), str(), etc. functions for explicit type conversion.
print("User input and type conversion examples executed successfully.")