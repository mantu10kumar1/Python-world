# Introduction to Basic Data Types in Python
'''
In Python, data types are used to define the type of data that a variable can hold. The most commonly used data types in Python include:
1. Integer (int): Represents whole numbers, both positive and negative, without decimal points.
2. Float (float): Represents real numbers with decimal points or in exponential form.
3. Boolean (bool): Represents one of two values: True or False.
4. String (str): Represents a sequence of characters enclosed in single, double, or triple quotes.
5. Complex Number (complex): Represents complex numbers with a real and imaginary part.
6. List (list): Represents an ordered collection of items, which can be of different data types, enclosed in square brackets.
7. Tuple (tuple): Represents an ordered, immutable collection of items, which can be of different data types, enclosed in parentheses.
8. Set (set): Represents an unordered collection of unique items, enclosed in curly braces.
9. Dictionary (dict): Represents a collection of key-value pairs, enclosed in curly braces, where each key is unique.
                Here are some examples of these data types in Python:

'''

# Integer
print(10)

print(1e309) # 1*10309

print(5.6)
print(1.5e309) # 1.5*10309

# Boolean
print(True)
print(False)

# There is no char datatype in Python. We use string datatype to represent single character also.

#String
print("Hello World")

# Complex Number
print(2 + 3j)

#List 
print([1,2,3,4,5])

# Tuple
print((1,2,3,4,5,6,7))

# Sets datatype
print({1,2,3,4,5})

# Dictionary datatype
print({"Name":"Mantu Kumar" , "Age" : 24})

# Let me print type of above datatypes
print(type(10))            # Integer
print(type(5.6))          # Float
print(type(True))         # Boolean
print(type("Hello"))      # String  
print(type(2 + 3j))      # Complex Number
print(type([1,2,3,4,5])) # List
print(type((1,2,3,4,5,6,7))) # Tuple
print(type({1,2,3,4,5})) # Set
print(type({"Name":"Mantu Kumar" , "Age" : 24})) # Dictionary
# You can also use the isinstance() function to check the data type of a variable
print(isinstance(10, int))            # Integer
print(isinstance(5.6, float))          # Float
