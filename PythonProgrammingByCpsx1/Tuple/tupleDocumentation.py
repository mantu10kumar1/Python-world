# Python Tuples Documentation

## Table of Contents

# 1. [Introduction to Tuples](#introduction)
# 2. [Tuple Creation](#creation)
# 3. [Tuple Indexing & Slicing](#indexing-slicing)
# 4. [Tuple Operations](#operations)
# 5. [Tuple Methods](#methods)
# 6. [Tuple Unpacking](#unpacking)
# 7. [Named Tuples](#named-tuples)
# 8. [Tuple vs List](#tuple-vs-list)
# 9. [Immutable Nature](#immutability)
# 10. [Practical Examples](#practical-examples)

## 1. Introduction to Tuples <a name="introduction"></a>
'''
Tuples are immutable, ordered collections of items in Python.
They are similar to lists but cannot be modified after creation.
Tuples are often used for fixed data that shouldn't change.
'''

'''
Key Characteristics:
- Immutable (cannot be changed after creation)
- Ordered (maintains insertion order)
- Fixed-size (cannot grow or shrink)
- Heterogeneous (can contain different types)
- Hashable (if all elements are hashable)
- Indexable and slicable
'''

# Example 1: Basic tuple
my_tuple = (1, 2, 3, "hello", 3.14, True)
print(type(my_tuple))                    # <class 'tuple'>
print(my_tuple)                          # (1, 2, 3, 'hello', 3.14, True)

## 2. Tuple Creation <a name="creation"></a>
'''
There are multiple ways to create tuples in Python:
1. Using parentheses
2. Without parentheses (tuple packing)
3. Using tuple() constructor
4. Creating nested tuples
'''

# Example 2: Different ways to create tuples
# Using parentheses
empty_tuple = ()
single_tuple = (42,)
numbers = (1, 2, 3, 4, 5)
fruits = ("apple", "banana", "cherry")

# Tuple packing (without parentheses)
my_tuple = 1, 2, 3, "hello"
single = 42,

# Using tuple() constructor
from_list = tuple([1, 2, 3])
from_string = tuple("hello")
from_range = tuple(range(5))

# Nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))

print("Empty tuple:", empty_tuple)                    # Empty tuple: ()
print("Single element tuple:", single_tuple)          # Single element tuple: (42,)
print("Tuple packing:", my_tuple)                     # Tuple packing: (1, 2, 3, 'hello')
print("From list:", from_list)                        # From list: (1, 2, 3)
print("Nested tuple:", nested_tuple)                  # Nested tuple: ((1, 2), (3, 4), (5, 6))

## 3. Tuple Indexing & Slicing <a name="indexing-slicing"></a>
'''
Tuples support indexing and slicing similar to lists.
Indexing starts from 0 for positive indices and -1 for negative indices.
Slicing creates new tuples since tuples are immutable.
'''

# Example 3: Indexing and slicing
fruits = ("apple", "banana", "cherry", "date", "elderberry")

# Positive indexing
print("First fruit:", fruits[0])                      # First fruit: apple
print("Third fruit:", fruits[2])                      # Third fruit: cherry

# Negative indexing
print("Last fruit:", fruits[-1])                      # Last fruit: elderberry
print("Second last:", fruits[-2])                     # Second last: date

# Slicing
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Slice 2:5:", numbers[2:5])                     # Slice 2:5: (2, 3, 4)
print("First 5:", numbers[:5])                        # First 5: (0, 1, 2, 3, 4)
print("From index 5:", numbers[5:])                   # From index 5: (5, 6, 7, 8, 9)
print("Every 2nd element:", numbers[::2])             # Every 2nd element: (0, 2, 4, 6, 8)
print("Reversed:", numbers[::-1])                     # Reversed: (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

## 4. Tuple Operations <a name="operations"></a>
'''
Tuples support various operations:
1. Concatenation (+ operator)
2. Repetition (* operator)
3. Comparison (==, !=, <, >, <=, >=)
4. Membership testing (in, not in)
5. Length, min, max, sum functions
'''

# Example 4: Tuple operations
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
result = tuple1 + tuple2
print("Concatenation:", result)                       # Concatenation: (1, 2, 3, 4, 5, 6)

# Repetition
repeated = tuple1 * 3
print("Repetition:", repeated)                        # Repetition: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Comparison
print("tuple1 == tuple2:", tuple1 == tuple2)          # tuple1 == tuple2: False
print("(1, 2, 3) < (1, 2, 4):", (1, 2, 3) < (1, 2, 4))   # (1, 2, 3) < (1, 2, 4): True

# Membership testing
fruits = ("apple", "banana", "cherry")
print("'banana' in fruits:", "banana" in fruits)      # 'banana' in fruits: True
print("'grape' not in fruits:", "grape" not in fruits) # 'grape' not in fruits: True

# Built-in functions
numbers = (10, 20, 30, 40, 50)
print("Length:", len(numbers))                        # Length: 5
print("Minimum:", min(numbers))                       # Minimum: 10
print("Maximum:", max(numbers))                       # Maximum: 50
print("Sum:", sum(numbers))                           # Sum: 150

## 5. Tuple Methods <a name="methods"></a>
'''
Tuples have only two methods:
1. count(): Count occurrences of a value
2. index(): Find first occurrence of a value
Tuples don't have modification methods since they are immutable.
'''

# Example 5: Tuple methods
numbers = (1, 2, 3, 2, 4, 2, 5, 2)

# count() method
print("Count of 2:", numbers.count(2))                # Count of 2: 4
print("Count of 7:", numbers.count(7))                # Count of 7: 0

# index() method
fruits = ("apple", "banana", "cherry", "banana", "date")
print("Index of 'banana':", fruits.index("banana"))   # Index of 'banana': 1
print("Index of 'banana' from position 2:", fruits.index("banana", 2)) # Index of 'banana' from position 2: 3

## 6. Tuple Unpacking <a name="unpacking"></a>
'''
Tuple unpacking allows assigning tuple elements to individual variables.
Extended unpacking (* operator) can capture multiple elements.
'''

# Example 6: Tuple unpacking
# Basic unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"x: {x}, y: {y}, z: {z}")                      # x: 10, y: 20, z: 30

# Extended unpacking
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}") # First: 1, Middle: [2, 3, 4], Last: 5

# Variable swapping
a, b = 10, 20
print(f"Before swap: a={a}, b={b}")                   # Before swap: a=10, b=20
a, b = b, a
print(f"After swap: a={a}, b={b}")                    # After swap: a=20, b=10

# Function return values
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

stats = get_stats((10, 20, 30, 40, 50))
minimum, maximum, average = stats
print(f"Min: {minimum}, Max: {maximum}, Avg: {average}") # Min: 10, Max: 50, Avg: 30.0

## 7. Named Tuples <a name="named-tuples"></a>
'''
Named tuples provide readable, self-documenting code.
They are subclass of tuples with named fields.

'''

# Example 7: Named tuples
from collections import namedtuple

# Create named tuple type
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instances
person1 = Person("Alice", 25, "New York")
person2 = Person(name="Bob", age=30, city="Los Angeles")

print("Person 1:", person1)                           # Person 1: Person(name='Alice', age=25, city='New York')
print("Person 2 name:", person2.name)                 # Person 2 name: Bob
print("Person 2 age:", person2.age)                   # Person 2 age: 30

# Named tuple methods
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print("As dict:", p._asdict())                        # As dict: {'x': 10, 'y': 20}
print("Replace x:", p._replace(x=100))                # Replace x: Point(x=100, y=20)
print("Fields:", Point._fields)                       # Fields: ('x', 'y')

# Modern syntax with type hints
from typing import NamedTuple

class Employee(NamedTuple):
    name: str
    id: int
    department: str = "Unassigned"

emp1 = Employee("Alice", 101, "Engineering")
emp2 = Employee("Bob", 102)
print("Employee 1:", emp1)                            # Employee 1: Employee(name='Alice', id=101, department='Engineering')
print("Employee 2:", emp2)                            # Employee 2: Employee(name='Bob', id=102, department='Unassigned')

## 8. Tuple vs List <a name="tuple-vs-list"></a>
'''
Key differences between tuples and lists:
- Tuples are immutable, lists are mutable
- Tuples use parentheses, lists use square brackets
- Tuples are faster and use less memory
- Tuples can be dictionary keys, lists cannot
'''

# Example 8: Comparison with lists
import sys
import timeit

# Memory comparison
list_data = [1, 2, 3]
tuple_data = (1, 2, 3)
print("List memory:", sys.getsizeof(list_data), "bytes") # List memory: 88 bytes
print("Tuple memory:", sys.getsizeof(tuple_data), "bytes") # Tuple memory: 64 bytes

# Performance comparison
list_time = timeit.timeit('[1, 2, 3, 4, 5]', number=1000000)
tuple_time = timeit.timeit('(1, 2, 3, 4, 5)', number=1000000)
print(f"List creation time: {list_time:.6f}")         # List creation time: 0.123456
print(f"Tuple creation time: {tuple_time:.6f}")       # Tuple creation time: 0.098765
print(f"Tuple is {list_time/tuple_time:.2f}x faster") # Tuple is 1.25x faster

# Hashability (dictionary keys)
valid_dict = {(1, 2): "value1", (3, 4): "value2"}
print("Tuple as dictionary keys:", valid_dict)        # Tuple as dictionary keys: {(1, 2): 'value1', (3, 4): 'value2'}

## 9. Immutable Nature <a name="immutability"></a>
'''
Tuples are immutable, meaning they cannot be changed after creation.
However, mutable objects inside tuples can be modified.
'''

# Example 9: Immutability demonstration
# Tuple itself is immutable
mixed_tuple = (1, [2, 3], {"key": "value"})

# Cannot modify tuple elements directly
# mixed_tuple[0] = 10  # This would raise TypeError

# But can modify mutable elements inside
mixed_tuple[1].append(4)  # Modify list inside tuple
mixed_tuple[2]["new_key"] = "new_value"  # Modify dict inside tuple
print("Modified mixed tuple:", mixed_tuple) # Modified mixed tuple: (1, [2, 3, 4], {'key': 'value', 'new_key': 'new_value'})

# Workarounds for "modifying" tuples
original = (1, 2, 3, 4, 5)

# "Add" element (concatenation)
new_tuple = original + (6,)
print("After adding 6:", new_tuple)                   # After adding 6: (1, 2, 3, 4, 5, 6)

# "Remove" element (slicing)
without_first = original[1:]
print("Without first:", without_first)                # Without first: (2, 3, 4, 5)

# "Replace" element
index_to_replace = 2
replaced = original[:index_to_replace] + (99,) + original[index_to_replace+1:]
print("After replacing index 2:", replaced)           # After replacing index 2: (1, 2, 99, 4, 5)

## 10. Practical Examples <a name="practical-examples"></a>
'''
Real-world applications of tuples:
1. RGB color codes
2. Coordinate systems
3. Database records
4. Function arguments and returns
5. Configuration settings
'''

# Example 10.1: RGB Color Codes
COLORS = {
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 0, 255),
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0)
}

def blend_colors(color1, color2, ratio=0.5):
    r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
    g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
    b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
    return (r, g, b)

red = COLORS["RED"]
blue = COLORS["BLUE"]
purple = blend_colors(red, blue, 0.5)
print("Purple color:", purple)                        # Purple color: (127, 0, 127)

# Example 10.2: Coordinate System
import math

Point2D = namedtuple('Point2D', ['x', 'y'])

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

p1 = Point2D(10, 20)
p2 = Point2D(30, 40)
print("Distance between points:", distance(p1, p2))   # Distance between points: 28.284271247461902

# Example 10.3: Database Records Simulation
def get_user_records():
    return [
        (1, "Alice", "alice@email.com", "2023-01-15"),
        (2, "Bob", "bob@email.com", "2023-02-20"),
        (3, "Charlie", "charlie@email.com", "2023-03-10")
    ]

records = get_user_records()
for user_id, name, email, join_date in records:
    print(f"ID: {user_id}, Name: {name}, Joined: {join_date}")
    '''
    Output:
    ID: 1, Name: Alice, Joined: 2023-01-15
    ID: 2, Name: Bob, Joined: 2023-02-20
    ID: 3, Name: Charlie, Joined: 2023-03-10
    '''

# Example 10.4: Function with Multiple Return Values
def analyze_numbers(numbers):
    if not numbers:
        return (0, 0, 0, 0, 0)
    
    return (
        len(numbers),
        min(numbers),
        max(numbers),
        sum(numbers),
        sum(numbers) / len(numbers)
    )

stats = analyze_numbers((10, 20, 30, 40, 50))
count, minimum, maximum, total, average = stats
print(f"Stats - Count: {count}, Min: {minimum}, Max: {maximum}, Total: {total}, Avg: {average:.2f}")
# Stats - Count: 5, Min: 10, Max: 50, Total: 150, Avg: 30.00

# Example 10.5: Configuration Settings
DATABASE_CONFIG = (
    "localhost",    # host
    5432,           # port
    "mydb",         # database
    "admin",        # username
    "secret123"     # password
)

def connect_to_database(config):
    host, port, database, username, password = config
    return f"Connected to {database}@{host}:{port}"

print(connect_to_database(DATABASE_CONFIG))          # Connected to mydb@localhost:5432