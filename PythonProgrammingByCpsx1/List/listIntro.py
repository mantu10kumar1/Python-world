'''Python Lists - Complete Documentation
Table of Contents
Introduction to Lists

List Creation

List Indexing & Slicing

List Methods

List Operations

List Comprehension

List Iteration

List vs Other Sequences

Nested Lists

List Unpacking

Sorting Lists

Copying Lists

Performance Considerations

Practical Examples

1. Introduction to Lists <a name="introduction"></a>
Definition: A list in Python is a mutable, ordered collection of items (elements) that can be of different data types. Lists are one of Python's most versatile and commonly used data structures.

Key Characteristics:

Mutable (can be changed after creation)

Ordered (maintains insertion order)

Dynamic (can grow or shrink)

Heterogeneous (can contain different types)

Indexable and slicable

Iterable (can be looped through)
'''

# python
# Basic list
my_list = [1, 2, 3, "hello", 3.14, True]
print(type(my_list))  # <class 'list'>
print(my_list)        # [1, 2, 3, 'hello', 3.14, True]
# 2. List Creation <a name="creation"></a>
# 2.1 Using Square Brackets
# python
# Empty list
empty_list = []
print(empty_list)  # []

# List with elements
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True, [1, 2, 3]]
# 2.2 Using list() Constructor
# python
# From string (iterable)
print(list("hello"))        # ['h', 'e', 'l', 'l', 'o']

# From tuple
print(list((1, 2, 3)))      # [1, 2, 3]

# From range
print(list(range(5)))       # [0, 1, 2, 3, 4]

# From set
print(list({1, 2, 3}))      # [1, 2, 3] (order may vary)

# From dictionary (keys only)
print(list({"a": 1, "b": 2}))  # ['a', 'b']

# Creating empty list
empty = list()
print(empty)  # []
# 2.3 Using List Multiplication
# python
# Create list with repeated elements
zeros = [0] * 5
print(zeros)  # [0, 0, 0, 0, 0]

fruits = ["apple"] * 3
print(fruits)  # ['apple', 'apple', 'apple']

# Be careful with mutable objects!
nested = [[]] * 3
print(nested)  # [[], [], []]
nested[0].append(1)
print(nested)  # [[1], [1], [1]] - All refer to same list!
# 3. List Indexing & Slicing <a name="indexing-slicing"></a>
# 3.1 Indexing
python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Positive indexing (0-based, left to right)
print(fruits[0])   # 'apple'
print(fruits[1])   # 'banana'
print(fruits[4])   # 'elderberry'

# Negative indexing (right to left)
print(fruits[-1])  # 'elderberry'
print(fruits[-2])  # 'date'
print(fruits[-5])  # 'apple'

# Index assignment (lists are mutable!)
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry', 'date', 'elderberry']
# 3.2 Slicing
# python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing: list[start:end:step]
print(numbers[2:5])     # [2, 3, 4] (index 2 to 4)
print(numbers[:5])      # [0, 1, 2, 3, 4] (start to index 4)
print(numbers[5:])      # [5, 6, 7, 8, 9] (index 5 to end)
print(numbers[:])       # Full list (shallow copy)
print(numbers[::2])     # [0, 2, 4, 6, 8] (every 2nd element)
print(numbers[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverse)
print(numbers[1:8:2])   # [1, 3, 5, 7] (from index 1 to 7, step 2)

# Slicing with assignment
numbers[2:5] = [20, 30, 40]
print(numbers)  # [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]

# Deleting elements with slice
numbers[2:5] = []
print(numbers)  # [0, 1, 5, 6, 7, 8, 9]
# 4. List Methods <a name="methods"></a>
# 4.1 Adding Elements
python
fruits = ["apple", "banana"]

# append() - add single element at end
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# extend() - add multiple elements from iterable
fruits.extend(["date", "elderberry"])
print(fruits)  # ['apple', 'banana', 'cherry', 'date', 'elderberry']

# insert() - insert element at specific position
fruits.insert(1, "blueberry")  # Insert at index 1
print(fruits)  # ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']
# 4.2 Removing Elements
# python
fruits = ["apple", "banana", "cherry", "banana", "date"]

# remove() - remove first occurrence of value
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'banana', 'date']

# pop() - remove and return element at index (default last)
last = fruits.pop()
print(last)    # 'date'
print(fruits)  # ['apple', 'cherry', 'banana']

second = fruits.pop(1)
print(second)  # 'cherry'
print(fruits)  # ['apple', 'banana']

# clear() - remove all elements
fruits.clear()
print(fruits)  # []
# 4.3 Finding Elements
# python
numbers = [10, 20, 30, 20, 40, 50]

# index() - find first occurrence
print(numbers.index(20))      # 1
print(numbers.index(20, 2))   # 3 (search from index 2)
print(numbers.index(20, 2, 4)) # 3 (search between index 2-3)

# count() - count occurrences
print(numbers.count(20))      # 2
print(numbers.count(100))     # 0

# in operator (membership test)
print(30 in numbers)          # True
print(100 in numbers)         # False

# not in operator
print(100 not in numbers)     # True
# 4.4 Reordering Elements
# python
numbers = [3, 1, 4, 1, 5, 9, 2]

# sort() - sort in place (ascending by default)
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 2, 1, 1]

# Custom sorting
words = ["apple", "Banana", "cherry", "Date"]
words.sort()  # Case-sensitive: uppercase first
print(words)  # ['Banana', 'Date', 'apple', 'cherry']

words.sort(key=str.lower)  # Case-insensitive
print(words)  # ['apple', 'Banana', 'cherry', 'Date']

# reverse() - reverse in place
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]
# 4.5 Copying Lists
# python
original = [1, 2, [3, 4]]

# copy() - shallow copy
shallow_copy = original.copy()
shallow_copy[2][0] = 99
print(original)  # [1, 2, [99, 4]] (nested list affected!)

# Methods that create new lists
numbers = [1, 2, 3, 4, 5]
new_list = list(numbers)  # Constructor
slice_copy = numbers[:]   # Slicing
# 5. List Operations <a name="operations"></a>
# 5.1 Concatenation
python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using + operator
result = list1 + list2
print(result)  # [1, 2, 3, 4, 5, 6]

# Using += operator
list1 += list2
print(list1)   # [1, 2, 3, 4, 5, 6]

# concat() method (Python 3.11+)
# Available as list.__add__ but not as concat() method
# 5.2 Repetition
# python
numbers = [1, 2, 3]
print(numbers * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Creating list with repeated elements
zeros = [0] * 5
print(zeros)  # [0, 0, 0, 0, 0]
# 5.3 Comparison
# python
# Element-wise comparison
print([1, 2, 3] == [1, 2, 3])    # True
print([1, 2, 3] == [1, 2, 4])    # False
print([1, 2, 3] != [1, 2, 4])    # True

# Lexicographical comparison
print([1, 2, 3] < [1, 2, 4])     # True (3 < 4)
print([1, 2, 3] < [1, 2, 3, 4])  # True (shorter list < longer list)
print([1, 2, 10] < [1, 2, 2])    # False (10 > 2)
# 5.4 Length, Minimum, Maximum, Sum
# python
numbers = [10, 20, 30, 40, 50]

print(len(numbers))   # 5 (length)
print(min(numbers))   # 10 (minimum)
print(max(numbers))   # 50 (maximum)
print(sum(numbers))   # 150 (sum)

# With strings
fruits = ["apple", "banana", "cherry"]
print(min(fruits))    # 'apple' (alphabetical)
print(max(fruits))    # 'cherry'
# 6. List Comprehension <a name="comprehension"></a>
# 6.1 Basic List Comprehension
python
# Traditional way
squares = []
for i in range(5):
    squares.append(i ** 2)
print(squares)  # [0, 1, 4, 9, 16]

# Using list comprehension
squares = [i ** 2 for i in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# More examples
even_numbers = [i for i in range(10) if i % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8]

words = ["hello", "world", "python"]
lengths = [len(word) for word in words]
print(lengths)  # [5, 5, 6]
# 6.2 Nested List Comprehension
# python
# Matrix (list of lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Flatten matrix
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Transpose matrix
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Cartesian product
colors = ["red", "green", "blue"]
sizes = ["S", "M", "L"]
combinations = [(color, size) for color in colors for size in sizes]
print(combinations)
# [('red', 'S'), ('red', 'M'), ('red', 'L'),
#  ('green', 'S'), ('green', 'M'), ('green', 'L'),
#  ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]
6.3 Conditional List Comprehension
python
numbers = [-3, -2, -1, 0, 1, 2, 3]

# With if condition
positive = [n for n in numbers if n > 0]
print(positive)  # [1, 2, 3]

# With if-else (ternary expression)
signs = ["positive" if n > 0 else "negative" if n < 0 else "zero" for n in numbers]
print(signs)  # ['negative', 'negative', 'negative', 'zero', 'positive', 'positive', 'positive']

# Multiple conditions
filtered = [n for n in numbers if n > 0 and n % 2 == 0]
print(filtered)  # [2]
7. List Iteration <a name="iteration"></a>
7.1 Basic Iteration
python
fruits = ["apple", "banana", "cherry"]

# Using for loop
for fruit in fruits:
    print(fruit)
# apple
# banana
# cherry

# Using enumerate() for index and value
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
# Index 0: apple
# Index 1: banana
# Index 2: cherry

# With custom start index
for index, fruit in enumerate(fruits, start=1):
    print(f"#{index}: {fruit}")
7.2 Iterating with zip()
python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

# Iterate over multiple lists simultaneously
for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")
# Alice is 25 years old and lives in NYC
# Bob is 30 years old and lives in LA
# Charlie is 35 years old and lives in Chicago

# Create list of tuples
combined = list(zip(names, ages))
print(combined)  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
# 7.3 Reverse Iteration
# python
numbers = [1, 2, 3, 4, 5]

# Using reversed() function
for num in reversed(numbers):
    print(num)  # 5, 4, 3, 2, 1

# Using negative step in range
for i in range(len(numbers)-1, -1, -1):
    print(numbers[i])  # 5, 4, 3, 2, 1
8. List vs Other Sequences <a name="vs-sequences"></a>
8.1 List vs Tuple
python
# List (mutable)
list_example = [1, 2, 3]
list_example[0] = 10  # OK
list_example.append(4)  # OK

# Tuple (immutable)
tuple_example = (1, 2, 3)
# tuple_example[0] = 10  # TypeError
# tuple_example.append(4)  # AttributeError

# When to use which?
# Use lists when you need to modify the collection
# Use tuples for fixed collections, dictionary keys, function returns
8.2 List vs String
python
# String (immutable, characters only)
string_example = "hello"
# string_example[0] = 'H'  # TypeError
new_string = "H" + string_example[1:]

# List (mutable, any type)
list_example = ['h', 'e', 'l', 'l', 'o']
list_example[0] = 'H'  # OK

# Convert between them
string_to_list = list("hello")  # ['h', 'e', 'l', 'l', 'o']
list_to_string = ''.join(['h', 'e', 'l', 'l', 'o'])  # 'hello'
9. Nested Lists <a name="nested-lists"></a>
9.1 Creating and Accessing
python
# 2D List (Matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(matrix[0][0])  # 1 (row 0, col 0)
print(matrix[1][2])  # 6 (row 1, col 2)
print(matrix[2][1])  # 8 (row 2, col 1)

# Modifying
matrix[1][1] = 50
print(matrix)  # [[1, 2, 3], [4, 50, 6], [7, 8, 9]]

# 3D List
cube = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]
print(cube[0][1][0])  # 3
9.2 Flattening Nested Lists
python
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# Using nested loops
flattened = []
for sublist in nested:
    for item in sublist:
        flattened.append(item)
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using list comprehension
flattened = [item for sublist in nested for item in sublist]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
10. List Unpacking <a name="unpacking"></a>
10.1 Basic Unpacking
python
# Unpacking into variables
colors = ["red", "green", "blue"]
c1, c2, c3 = colors
print(c1, c2, c3)  # red green blue

# Using star (*) operator
first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# Ignoring elements with underscore
data = ["Alice", 25, "NYC", "Engineer"]
name, age, *_ = data
print(name, age)  # Alice 25
10.2 Extended Unpacking
python
# Swapping variables
a, b = 10, 20
print(f"Before: a={a}, b={b}")  # Before: a=10, b=20
a, b = b, a
print(f"After: a={a}, b={b}")   # After: a=20, b=10

# Merging lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = [*list1, *list2]
print(merged)  # [1, 2, 3, 4, 5, 6]

# Function arguments
def sum_numbers(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(sum_numbers(*numbers))  # 6
11. Sorting Lists <a name="sorting"></a>
11.1 Basic Sorting
python
numbers = [5, 2, 9, 1, 5, 6]

# sort() - in place (modifies original)
numbers.sort()
print(numbers)  # [1, 2, 5, 5, 6, 9]

numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 5, 2, 1]

# sorted() - returns new sorted list
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(original)     # [3, 1, 4, 1, 5] (unchanged)
print(sorted_list)  # [1, 1, 3, 4, 5]
11.2 Custom Sorting
python
# Sorting strings
fruits = ["apple", "Banana", "cherry", "Date"]
fruits.sort()  # Case-sensitive
print(fruits)  # ['Banana', 'Date', 'apple', 'cherry']

fruits.sort(key=str.lower)  # Case-insensitive
print(fruits)  # ['apple', 'Banana', 'cherry', 'Date']

# Sorting by length
fruits.sort(key=len)
print(fruits)  # ['Date', 'apple', 'cherry', 'Banana']

# Sorting dictionaries in list
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]

people.sort(key=lambda x: x["age"])
print(people)
# [{'name': 'Charlie', 'age': 20},
#  {'name': 'Alice', 'age': 25},
#  {'name': 'Bob', 'age': 30}]

# Multiple sort criteria
students = [
    ("Alice", "B", 25),
    ("Bob", "A", 30),
    ("Charlie", "B", 20),
    ("David", "A", 25)
]

# Sort by grade, then age
students.sort(key=lambda x: (x[1], x[2]))
print(students)
# [('David', 'A', 25), ('Bob', 'A', 30), ('Charlie', 'B', 20), ('Alice', 'B', 25)]
12. Copying Lists <a name="copying"></a>
12.1 Shallow Copy
python
original = [1, 2, [3, 4]]

# These create shallow copies
shallow1 = original.copy()
shallow2 = list(original)
shallow3 = original[:]

# Modifying top level
shallow1[0] = 99
print(original)   # [1, 2, [3, 4]] (unchanged)
print(shallow1)   # [99, 2, [3, 4]]

# Modifying nested object affects all!
shallow1[2][0] = 999
print(original)   # [1, 2, [999, 4]] (changed!)
print(shallow1)   # [99, 2, [999, 4]]
12.2 Deep Copy
python
import copy

original = [1, 2, [3, 4]]

# Deep copy
deep_copy = copy.deepcopy(original)

# Now nested objects are independent
deep_copy[2][0] = 999
print(original)   # [1, 2, [3, 4]] (unchanged)
print(deep_copy)  # [1, 2, [999, 4]]
13. Performance Considerations <a name="performance"></a>
13.1 Time Complexity
python
"""
Common List Operations Time Complexity:
- Access by index: O(1)
- Append: O(1)
- Pop last: O(1)
- Pop intermediate: O(n)
- Insert: O(n)
- Search (in operator): O(n)
- Slice: O(k) where k is slice size
- Sort: O(n log n)
- Copy: O(n)
"""
13.2 Memory Optimization
python
# Use generators for large sequences
def large_sequence():
    for i in range(1000000):
        yield i

# Instead of
# big_list = list(range(1000000))  # Uses lots of memory

# Use array module for homogeneous numeric data
import array
numbers = array.array('i', [1, 2, 3, 4, 5])  # More memory efficient
# 14. Practical Examples <a name="practical-examples"></a>
# Example 1: Matrix Operations
python
def matrix_transpose(matrix):
    """Transpose a matrix (list of lists)"""
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def matrix_multiply(A, B):
    """Multiply two matrices"""
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Usage
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(matrix_transpose(A))  # [[1, 3], [2, 4]]
print(matrix_multiply(A, B))  # [[19, 22], [43, 50]]
Example 2: Stack and Queue Implementation
python
# Stack (LIFO) using list
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
print(stack.pop())  # 3 (Pop)
print(stack.pop())  # 2

# Queue (FIFO) using collections.deque (more efficient)
from collections import deque
queue = deque()
queue.append(1)  # Enqueue
queue.append(2)
queue.append(3)
print(queue.popleft())  # 1 (Dequeue)
print(queue.popleft())  # 2
Example 3: Removing Duplicates
python
def remove_duplicates(lst):
    """Remove duplicates while preserving order"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Or using dict (Python 3.7+ preserves insertion order)
def remove_duplicates_simple(lst):
    return list(dict.fromkeys(lst))

numbers = [1, 2, 2, 3, 4, 4, 5, 1]
print(remove_duplicates(numbers))        # [1, 2, 3, 4, 5]
print(remove_duplicates_simple(numbers)) # [1, 2, 3, 4, 5]
Example 4: List Chunking
python
def chunk_list(lst, chunk_size):
    """Split list into chunks of specified size"""
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def chunk_generator(lst, chunk_size):
    """Generator version for memory efficiency"""
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

numbers = list(range(10))
print(chunk_list(numbers, 3))
# [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

for chunk in chunk_generator(numbers, 4):
    print(chunk)
# [0, 1, 2, 3]
# [4, 5, 6, 7]
# [8, 9]
Example 5: Frequency Counter
python
def frequency_counter(lst):
    """Count frequency of elements in list"""
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

def most_common(lst):
    """Find most common element in list"""
    if not lst:
        return None
    freq = frequency_counter(lst)
    return max(freq, key=freq.get)

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print(frequency_counter(words))
# {'apple': 3, 'banana': 2, 'cherry': 1}
print(most_common(words))  # apple
Example 6: List Difference Operations
python
def list_difference(list1, list2):
    """Elements in list1 but not in list2"""
    set2 = set(list2)
    return [item for item in list1 if item not in set2]

def symmetric_difference(list1, list2):
    """Elements in either list but not in both"""
    set1, set2 = set(list1), set(list2)
    return list((set1 - set2) | (set2 - set1))

A = [1, 2, 3, 4, 5]
B = [4, 5, 6, 7, 8]

print(list_difference(A, B))      # [1, 2, 3]
print(list_difference(B, A))      # [6, 7, 8]
print(symmetric_difference(A, B)) # [1, 2, 3, 6, 7, 8]
Example 7: Flatten Irregular Lists
python
def flatten_irregular(lst):
    """Flatten irregular nested lists using recursion"""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_irregular(item))
        else:
            result.append(item)
    return result

irregular = [1, [2, [3, 4], 5], 6, [7, 8]]
print(flatten_irregular(irregular))  # [1, 2, 3, 4, 5, 6, 7, 8]

# Using recursion limit
def flatten_with_depth(lst, max_depth=10):
    def helper(items, depth):
        if depth > max_depth:
            raise RecursionError("Maximum recursion depth exceeded")
        result = []
        for item in items:
            if isinstance(item, list):
                result.extend(helper(item, depth + 1))
            else:
                result.append(item)
        return result
    return helper(lst, 0)
Summary
Python lists are extremely versatile and powerful data structures:

Mutable & Dynamic: Can be modified after creation

Heterogeneous: Can contain any data type

Rich Methods: append(), extend(), insert(), remove(), pop(), sort(), reverse(), etc.

List Comprehensions: Concise way to create and transform lists

Multiple Ways to Copy: Shallow vs deep copy depending on needs

Performance: O(1) for many operations but O(n) for insertions/deletions in middle

Versatile Applications: Can implement stacks, queues, matrices, and more

Lists are fundamental to Python programming and mastering them is essential for writing efficient, readable code. Always consider using list comprehensions for transformations, and be mindful of shallow vs deep copies when working with nested lists.