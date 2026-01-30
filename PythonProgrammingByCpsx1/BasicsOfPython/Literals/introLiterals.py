# Literals in Python
# What are Literals?
# Literals are the fixed values assigned to variables or constants in a program.
# They represent the actual data that is stored in memory.
# Types of Literals in Python
# 1. Numeric Literals: These include integer literals (e.g., 10, -5) and floating-point literals (e.g., 3.14, -0.5).
# 2. String Literals: These are sequences of characters enclosed in single quotes (' '),
#  double quotes (" "), or triple quotes (''' ''' or """ """).
# 3. Boolean Literals: These represent the two boolean values: True and False.
# 4. Special Literals: Python has a special literal called None, which represents the absence of a value.
# Examples of Literals in Python
# Numeric Literals
int_literal = 10
float_literal = 3.14
print("Integer Literal: ", int_literal)
print("Float Literal: ", float_literal)

# Floating Point Literals
float_num1 = 1.5e2  # 1.5 * 10^2 = 150.0
float_num2 = -2.5e-3 # -2.5 * 10^-3 = -0.0025
print("Floating Point Literal 1: ", float_num1)
print("Floating Point Literal 2: ", float_num2)

# String Literals
single_quote_string = 'Hello'
double_quote_string = "World"
triple_quote_string = '''This is a
triple-quoted string.'''
unicode_string = u'Unicode String'
raw_string = r'Raw\nString'
print("Single Quote String: ", single_quote_string)
print("Double Quote String: ", double_quote_string)
print("Triple Quote String: ", triple_quote_string)
print("Unicode String: ", unicode_string)
print("Raw String: ", raw_string)

# Complex Literals
complex_literal = 2 + 3j
print("Complex Literal: ", complex_literal)
x = complex(4, 5)
print("Complex Literal using complex(): ", x)

x = 3 + 4j
print("Real part:", x.real) # Output: 3.0
print("Imaginary part:", x.imag) # Output: 4.0

# Boolean Literals
bool_true = True
bool_false = False
print("Boolean True: ", bool_true)
print("Boolean False: ", bool_false)

a  = True + 4
b = False + 10
print("True + 4 = ", a)   # Output: 5
print("False + 10 = ", b) # Output: 10


# Special Literal
none_literal = None
print("None Literal: ", none_literal)
print("Literals examples executed successfully.")

k 
a = 5 
b = 10
# We can not declare a variable if we declare a variable we will get an error
# as "SyntaxError: invalid syntax"
# So, we can say that literals are fixed values and we can use them to assign values to variables.
# By using None literal we can represent the absence of a value in a variable.

# Binary Literals
binary_literal = 0b1010  # Represents the decimal value 10
print("Binary Literal (0b1010): ", binary_literal)
# Octal Literals
octal_literal = 0o12     # Represents the decimal value 10
print("Octal Literal (0o12): ", octal_literal)
# Hexadecimal Literals
hexadecimal_literal = 0xA  # Represents the decimal value 10
print("Hexadecimal Literal (0xA): ", hexadecimal_literal)
print("Additional Literals examples executed successfully.")



# Summary of above code
# 1. Literals are fixed values assigned to variables or constants in a program.
# 2. Python supports various types of literals including numeric, string, boolean, and special literals.
# 3. Numeric literals can be integers or floating-point numbers.

# 4. String literals can be enclosed in single, double, or triple quotes.
# 5. Boolean literals represent True and False values.