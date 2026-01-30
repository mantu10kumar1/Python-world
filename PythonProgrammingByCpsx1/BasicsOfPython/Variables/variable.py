

# Variables
# In C and C++, we need to declare a variable before using it. But in Python, we can directly assign a value to a variable without declaring it first.
# int a = 10  # In C/C++
name = "Nitish"
print(name)

a = 5 
b = 6 
print(a + b)

# Dynamic Typing
# Python is a dynamically typed language, which means that we can change the data type of a variable at runtime.
x = 10      # x is an integer   
x = "Hello" # x is now a string

# Static Typing
# In statically typed languages like C and C++, we need to declare the data type of a variable before using it.
# int y = 10; // In C/C++

a = "Nitish"
print(a)

# Dynamic Binding
# In Python, variables are dynamically bound to objects. This means that the type of the variable is determined at runtime based
#  on the object it is bound to.
x = 10
print(type(x)) # Output: <class 'int'>

# Type of variable declaration
x = 10        # x is an integer
y = "Hello"   # y is a string
a , b , c = 1 , 2 , 3  # Multiple variable declaration
print(a  , b , c)

a = b = c = 10  # Multiple variable declaration with same value
print(a , b , c)

# Constants
# In Python, we can use uppercase letters to indicate that a variable is a constant and should
# not be changed. However, this is just a convention and Python does not enforce it.
PI = 3.14
GRAVITY = 9.8
print(PI)
print(GRAVITY)

# Variable Naming Rules
# 1. Variable names can contain letters, digits, and underscores (_).
# 2. Variable names must start with a letter or an underscore (_).
# 3. Variable names are case-sensitive (e.g., myVar and myvar are different variables).
# 4. Variable names cannot be the same as Python keywords (e.g., if, else, while, etc.).
my_var = 10
_myVar = 20
var123 = 30
print(my_var , _myVar , var123)

# Invalid variable names
# 1var = 10      # Invalid: starts with a digit
# my-var = 20    # Invalid: contains a hyphen
# my var = 30    # Invalid: contains a space
# if = 40        # Invalid: 'if' is a Python keyword
print("Variable naming rules examples executed successfully.")

# Python is case-sensitive
var = 10
Var = 20
print(var)  # Output: 10
print(Var)  # Output: 20
print("Case sensitivity example executed successfully.")
