# List Comprehension in Python - Complete Guide

## What is List Comprehension?
**List comprehension** is a concise, elegant way to create lists in Python. It provides a shorter syntax to create a new list based on existing iterables (like lists, tuples, strings, ranges, etc.). 

### Basic Syntax:
```python
new_list = [expression for item in iterable if condition]
```

This is equivalent to:
```python
new_list = []
for item in iterable:
    if condition:
        new_list.append(expression)
```

---

## 1. Basic List Comprehension Examples

### Example 1: Creating a List of Squares
```python
# Traditional approach
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(squares)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Using list comprehension
squares = [i ** 2 for i in range(1, 11)]
print(squares)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### Example 2: Converting to Uppercase
```python
words = ['hello', 'world', 'python', 'programming']

# Traditional approach
upper_words = []
for word in words:
    upper_words.append(word.upper())
print(upper_words)
# Output: ['HELLO', 'WORLD', 'PYTHON', 'PROGRAMMING']

# Using list comprehension
upper_words = [word.upper() for word in words]
print(upper_words)
# Output: ['HELLO', 'WORLD', 'PYTHON', 'PROGRAMMING']
```

### Example 3: Extracting First Letters
```python
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

first_letters = [fruit[0] for fruit in fruits]
print(first_letters)
# Output: ['a', 'b', 'c', 'd', 'e']
```

---

## 2. List Comprehension with Condition (Filtering)

### Example 4: Even Numbers Only
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Traditional approach
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(evens)
# Output: [2, 4, 6, 8, 10]

# Using list comprehension
evens = [num for num in numbers if num % 2 == 0]
print(evens)
# Output: [2, 4, 6, 8, 10]
```

### Example 5: Words Longer Than 5 Characters
```python
words = ['apple', 'banana', 'kiwi', 'strawberry', 'grape', 'watermelon']

long_words = [word for word in words if len(word) > 5]
print(long_words)
# Output: ['banana', 'strawberry', 'watermelon']
```

### Example 6: Numbers Divisible by 3 or 5
```python
numbers = range(1, 21)

divisible = [num for num in numbers if num % 3 == 0 or num % 5 == 0]
print(divisible)
# Output: [3, 5, 6, 9, 10, 12, 15, 18, 20]
```

---

## 3. List Comprehension with if-else (Conditional Expression)

### Example 7: Replace Negative with Zero
```python
numbers = [-5, -2, 0, 3, 7, -1, 4]

# Traditional approach
result = []
for num in numbers:
    if num < 0:
        result.append(0)
    else:
        result.append(num)
print(result)
# Output: [0, 0, 0, 3, 7, 0, 4]

# Using list comprehension with if-else
result = [0 if num < 0 else num for num in numbers]
print(result)
# Output: [0, 0, 0, 3, 7, 0, 4]
```

### Example 8: Classify Numbers as Even/Odd
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

classification = ['even' if num % 2 == 0 else 'odd' for num in numbers]
print(classification)
# Output: ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']
```

### Example 9: Pass/Fail Classification
```python
scores = [45, 89, 32, 67, 92, 55, 74]

result = ['Pass' if score >= 50 else 'Fail' for score in scores]
print(result)
# Output: ['Fail', 'Pass', 'Fail', 'Pass', 'Pass', 'Pass', 'Pass']
```

---

## 4. Nested List Comprehension

### Example 10: Flatten a Matrix
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Traditional approach
flattened = []
for row in matrix:
    for num in row:
        flattened.append(num)
print(flattened)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using nested list comprehension
flattened = [num for row in matrix for num in row]
print(flattened)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Example 11: Transpose a Matrix
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)
# Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

### Example 12: Cartesian Product
```python
colors = ['red', 'green', 'blue']
sizes = ['S', 'M', 'L']

# Traditional approach
combinations = []
for color in colors:
    for size in sizes:
        combinations.append((color, size))
print(combinations)
# Output: [('red', 'S'), ('red', 'M'), ('red', 'L'), 
#          ('green', 'S'), ('green', 'M'), ('green', 'L'), 
#          ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]

# Using list comprehension
combinations = [(color, size) for color in colors for size in sizes]
print(combinations)
# Output: [('red', 'S'), ('red', 'M'), ('red', 'L'), 
#          ('green', 'S'), ('green', 'M'), ('green', 'L'), 
#          ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]
```

---

## 5. Multiple Conditions in List Comprehension

### Example 13: Numbers Between 20 and 50 That Are Even
```python
numbers = [15, 22, 37, 42, 58, 29, 46, 33, 50]

filtered = [num for num in numbers if 20 <= num <= 50 if num % 2 == 0]
print(filtered)
# Output: [22, 42, 46, 50]

# Alternative syntax
filtered = [num for num in numbers if 20 <= num <= 50 and num % 2 == 0]
print(filtered)
# Output: [22, 42, 46, 50]
```

### Example 14: Words Starting with Vowel and Length > 4
```python
words = ['apple', 'banana', 'egg', 'orange', 'umbrella', 'ink', 'ocean']

filtered = [word for word in words 
           if word[0].lower() in 'aeiou' 
           if len(word) > 4]
print(filtered)
# Output: ['apple', 'orange', 'umbrella', 'ocean']
```

---

## 6. List Comprehension with Functions

### Example 15: Apply Function to Elements
```python
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]

squared = [square(num) for num in numbers]
print(squared)
# Output: [1, 4, 9, 16, 25]
```

### Example 16: Using Lambda Functions
```python
numbers = [1, 2, 3, 4, 5]

# Cube of numbers
cubes = [(lambda x: x ** 3)(num) for num in numbers]
print(cubes)
# Output: [1, 8, 27, 64, 125]

# Alternative: Define lambda separately
cube_func = lambda x: x ** 3
cubes = [cube_func(num) for num in numbers]
print(cubes)
# Output: [1, 8, 27, 64, 125]
```

### Example 17: Using Built-in Functions
```python
words = ['apple', 'banana', 'cherry']

# Length of each word
lengths = [len(word) for word in words]
print(lengths)
# Output: [5, 6, 6]

# Convert to title case
titles = [word.title() for word in words]
print(titles)
# Output: ['Apple', 'Banana', 'Cherry']
```

---

## 7. List Comprehension with Multiple Iterables

### Example 18: Element-wise Addition
```python
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]

result = [x + y for x, y in zip(list1, list2)]
print(result)
# Output: [11, 22, 33, 44]
```

### Example 19: Create Pairs from Two Lists
```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

pairs = [(name, age) for name, age in zip(names, ages)]
print(pairs)
# Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

### Example 20: Nested Loops with Multiple Lists
```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

combinations = [(x, y) for x in list1 for y in list2]
print(combinations)
# Output: [(1, 'a'), (1, 'b'), (1, 'c'), 
#          (2, 'a'), (2, 'b'), (2, 'c'), 
#          (3, 'a'), (3, 'b'), (3, 'c')]
```

---

## 8. Real-World Practical Examples

### Example 21: Extract File Extensions
```python
filenames = ['document.pdf', 'image.jpg', 'script.py', 'data.csv', 'report.docx']

extensions = [filename.split('.')[-1] for filename in filenames]
print(extensions)
# Output: ['pdf', 'jpg', 'py', 'csv', 'docx']
```

### Example 22: Process User Data
```python
users = [
    {'name': 'Alice', 'age': 25, 'active': True},
    {'name': 'Bob', 'age': 30, 'active': False},
    {'name': 'Charlie', 'age': 35, 'active': True},
    {'name': 'Diana', 'age': 28, 'active': True}
]

# Get names of active users
active_users = [user['name'] for user in users if user['active']]
print(active_users)
# Output: ['Alice', 'Charlie', 'Diana']

# Get names of users over 25
over_25 = [user['name'] for user in users if user['age'] > 25]
print(over_25)
# Output: ['Bob', 'Charlie', 'Diana']
```

### Example 23: Data Cleaning
```python
# Remove empty strings and strip whitespace
data = ['  apple  ', 'banana', '', '  cherry  ', '   ', 'date']

cleaned = [item.strip() for item in data if item.strip()]
print(cleaned)
# Output: ['apple', 'banana', 'cherry', 'date']
```

### Example 24: Convert Temperature
```python
# Celsius to Fahrenheit
celsius_temps = [0, 10, 20, 30, 40]

fahrenheit_temps = [(c * 9/5) + 32 for c in celsius_temps]
print(fahrenheit_temps)
# Output: [32.0, 50.0, 68.0, 86.0, 104.0]
```

### Example 25: Generate Multiplication Table
```python
n = 5
table = [[i * j for j in range(1, 11)] for i in range(1, n+1)]
for row in table:
    print(row)
# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
```

---

## 9. Advanced Examples

### Example 26: Find Common Elements in Multiple Lists
```python
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

common = [x for x in list1 if x in list2 and x in list3]
print(common)
# Output: [5]
```

### Example 27: Remove Duplicates While Preserving Order
```python
data = [1, 2, 2, 3, 4, 4, 5, 1, 2, 6]

# Traditional approach
unique = []
for item in data:
    if item not in unique:
        unique.append(item)
print(unique)
# Output: [1, 2, 3, 4, 5, 6]

# Using list comprehension (less efficient but concise)
unique = []
[unique.append(x) for x in data if x not in unique]
print(unique)
# Output: [1, 2, 3, 4, 5, 6]

# Better alternative (Python 3.6+): Use dict
unique = list(dict.fromkeys(data))
print(unique)
# Output: [1, 2, 3, 4, 5, 6]
```

### Example 28: Nested List Comprehension with Conditions
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Get even numbers from matrix
even_numbers = [num for row in matrix for num in row if num % 2 == 0]
print(even_numbers)
# Output: [2, 4, 6, 8]
```

### Example 29: Dictionary to List Conversion
```python
student_scores = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'Diana': 95
}

# Get names of students with score > 90
top_students = [name for name, score in student_scores.items() if score > 90]
print(top_students)
# Output: ['Bob', 'Diana']

# Convert to list of tuples
score_tuples = [(name, score) for name, score in student_scores.items()]
print(score_tuples)
# Output: [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('Diana', 95)]
```

---

## 10. Performance Comparison

```python
import time

# Create a large list
n = 1000000

# Method 1: Traditional loop
start = time.time()
squares1 = []
for i in range(n):
    squares1.append(i ** 2)
time1 = time.time() - start

# Method 2: List comprehension
start = time.time()
squares2 = [i ** 2 for i in range(n)]
time2 = time.time() - start

print(f"Traditional loop: {time1:.4f} seconds")
print(f"List comprehension: {time2:.4f} seconds")
print(f"List comprehension is {time1/time2:.2f}x faster")

# Output (example):
# Traditional loop: 0.1234 seconds
# List comprehension: 0.0987 seconds
# List comprehension is 1.25x faster
```

---

## Key Advantages of List Comprehension:
1. **Concise**: Less code, more readable
2. **Faster**: Generally faster than traditional loops
3. **Pythonic**: Considered more "Pythonic" and elegant
4. **Functional**: Encourages functional programming style

## When NOT to Use List Comprehension:
1. **Complex logic**: If the logic is too complex, a regular loop is better
2. **Multiple conditions**: When you have many nested if-else conditions
3. **Side effects**: If you need side effects (like printing during iteration)
4. **Readability**: If it reduces readability, use a regular loop

## Syntax Variations:
```python
# Basic
[expression for item in iterable]

# With condition
[expression for item in iterable if condition]

# With if-else
[expression1 if condition else expression2 for item in iterable]

# Nested
[expression for sublist in outer_list for item in sublist]

# Multiple conditions
[expression for item in iterable if condition1 if condition2]
```

List comprehension is a powerful feature that makes Python code more concise, readable, and efficient when used appropriately!