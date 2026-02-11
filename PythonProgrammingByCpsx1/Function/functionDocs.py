# Python Functions Documentation

## Table of Contents
# 1. [Introduction to Functions](#introduction)
# 2. [Function Definition & Calling](#definition-calling)
# 3. [Function Parameters & Arguments](#parameters-arguments)
# 4. [Return Statement](#return-statement)
# 5. [Types of Functions](#types-functions)
# 6. [Scope & Lifetime](#scope-lifetime)
# 7. [Lambda Functions](#lambda-functions)
# 8. [Recursion](#recursion)
# 9. [Decorators](#decorators)
# 10. [Generators](#generators)
# 11. [Built-in Functions](#built-in-functions)
# 12. [Practical Examples](#practical-examples)

## 1. Introduction to Functions <a name="introduction"></a>
'''
Functions are reusable blocks of code that perform a specific task.
They help in code organization, reusability, and modularity.
Functions can take inputs (parameters) and return outputs.
'''

'''
Key Characteristics:
- Reusable code blocks
- Can take parameters
- Can return values
- Help avoid code duplication
- Make code modular and maintainable
- Can be assigned to variables
'''

# Example 1: Basic function
def greet():
    """Simple function that prints greeting"""
    print("Hello, World!")

print(type(greet))                                 # <class 'function'>
greet()                                            # Hello, World!

## 2. Function Definition & Calling <a name="definition-calling"></a>
'''
Function definition syntax:
def function_name(parameters):
    """docstring"""
    function_body
    return value
'''

# Example 2: Function structure
def add_numbers(a, b):
    """
    Add two numbers and return result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    result = a + b
    return result

print(add_numbers.__doc__)                         # Add two numbers and return result...
print(add_numbers(5, 3))                           # 8

# Example 3: Function calling variations
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

# Positional arguments
display_info("Alice", 25)                          # Name: Alice, Age: 25

# Keyword arguments
display_info(age=30, name="Bob")                  # Name: Bob, Age: 30

# Mixed arguments
display_info("Charlie", age=35)                   # Name: Charlie, Age: 35

## 3. Function Parameters & Arguments <a name="parameters-arguments"></a>
'''
Python supports multiple types of parameters:
1. Required/Positional parameters
2. Default parameters
3. Variable-length parameters (*args, **kwargs)
4. Keyword-only parameters
5. Positional-only parameters
'''

# Example 4: Default parameters
def greet_user(name, greeting="Hello", punctuation="!"):
    """Function with default parameters"""
    return f"{greeting}, {name}{punctuation}"

print(greet_user("Alice"))                         # Hello, Alice!
print(greet_user("Bob", "Hi"))                     # Hi, Bob!
print(greet_user("Charlie", "Hey", "."))           # Hey, Charlie.

# Example 5: Variable-length arguments (*args)
def sum_all(*args):
    """Function that accepts variable number of positional arguments"""
    print(f"Arguments: {args}")
    print(f"Type of args: {type(args)}")
    return sum(args)

print(sum_all(1, 2, 3))                            # Arguments: (1, 2, 3)
                                                   # Type of args: <class 'tuple'>
                                                   # 6
print(sum_all(1, 2, 3, 4, 5))                     # Arguments: (1, 2, 3, 4, 5)
                                                   # Type of args: <class 'tuple'>
                                                   # 15

# Example 6: Variable-length keyword arguments (**kwargs)
def display_details(**kwargs):
    """Function that accepts variable number of keyword arguments"""
    print(f"Keyword arguments: {kwargs}")
    print(f"Type of kwargs: {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_details(name="Alice", age=25, city="NYC")
'''
Keyword arguments: {'name': 'Alice', 'age': 25, 'city': 'NYC'}
Type of kwargs: <class 'dict'>
name: Alice
age: 25
city: NYC
'''

# Example 7: Mixed parameter types
def complex_function(a, b, *args, c=10, d=20, **kwargs):
    """Function with positional, *args, default, and **kwargs parameters"""
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"c: {c}, d: {d}")
    print(f"kwargs: {kwargs}")

complex_function(1, 2, 3, 4, 5, c=30, e=40, f=50)
'''
a: 1, b: 2
args: (3, 4, 5)
c: 30, d: 20
kwargs: {'e': 40, 'f': 50}
'''

# Example 8: Keyword-only arguments (Python 3+)
def keyword_only_function(*, name, age):
    """Function with keyword-only arguments (after *)"""
    print(f"Name: {name}, Age: {age}")

keyword_only_function(name="Alice", age=25)        # Name: Alice, Age: 25
# keyword_only_function("Alice", 25)  # TypeError: takes 0 positional arguments

# Example 9: Positional-only arguments (Python 3.8+)
def positional_only_function(a, b, /, c, d):
    """Function with positional-only arguments (before /)"""
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")

positional_only_function(1, 2, 3, 4)              # a: 1, b: 2, c: 3, d: 4
positional_only_function(1, 2, c=3, d=4)          # a: 1, b: 2, c: 3, d: 4
# positional_only_function(a=1, b=2, c=3, d=4)    # TypeError: a and b are positional-only

## 4. Return Statement <a name="return-statement"></a>
'''
Return statement is used to exit a function and return a value.
Functions without return statement return None.
Multiple values can be returned as tuple.
'''

# Example 10: Return values
def no_return():
    """Function with no return statement"""
    print("This function has no return")

def single_return():
    """Function returning single value"""
    return 42

def multiple_return():
    """Function returning multiple values"""
    return 10, 20, 30  # Returns as tuple

print(no_return())                                 # This function has no return
                                                   # None
print(single_return())                             # 42
print(multiple_return())                           # (10, 20, 30)

# Example 11: Early return
def check_positive(number):
    """Function with early return"""
    if number <= 0:
        return "Negative or zero"
    return f"Positive: {number}"

print(check_positive(5))                           # Positive: 5
print(check_positive(-3))                          # Negative or zero

# Example 12: Returning complex data structures
def get_student_data():
    """Return dictionary with student information"""
    return {
        "name": "Alice",
        "age": 20,
        "courses": ["Math", "Physics"],
        "grades": {"Math": 95, "Physics": 88}
    }

student = get_student_data()
print(student)                                     # {'name': 'Alice', 'age': 20, 'courses': ['Math', 'Physics'], 'grades': {'Math': 95, 'Physics': 88}}

## 5. Types of Functions <a name="types-functions"></a>
'''
Functions can be categorized based on their purpose:
1. Built-in functions
2. User-defined functions
3. Anonymous functions (lambda)
4. Higher-order functions
5. Recursive functions
6. Generator functions
7. Inner functions
'''

# Example 13: Built-in functions
print("len([1,2,3]):", len([1, 2, 3]))             # len([1,2,3]): 3
print("max(10,20,30):", max(10, 20, 30))           # max(10,20,30): 30
print("type(42):", type(42))                       # type(42): <class 'int'>

# Example 14: User-defined functions
def calculate_rectangle_area(length, width):
    """Calculate area of rectangle"""
    return length * width

def calculate_circle_area(radius):
    """Calculate area of circle"""
    import math
    return math.pi * radius ** 2

print("Rectangle area:", calculate_rectangle_area(5, 3))  # Rectangle area: 15
print("Circle area:", calculate_circle_area(7))           # Circle area: 153.93804002589985

# Example 15: Inner functions (Nested functions)
def outer_function(text):
    """Outer function with inner function"""
    def inner_function():
        """Inner function that has access to outer variable"""
        return f"Inner says: {text}"
    
    return inner_function()

print(outer_function("Hello"))                     # Inner says: Hello

# Example 16: Functions as first-class citizens
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

# Assign function to variable
operation = square
print("Operation(5):", operation(5))               # Operation(5): 25

# Store functions in list
operations = [square, cube]
for op in operations:
    print(op(4))                                   # 16
                                                   # 64

# Return function from function
def get_power_function(exponent):
    def power(base):
        return base ** exponent
    return power

square_func = get_power_function(2)
cube_func = get_power_function(3)

print("Square of 5:", square_func(5))              # Square of 5: 25
print("Cube of 5:", cube_func(5))                 # Cube of 5: 125

## 6. Scope & Lifetime <a name="scope-lifetime"></a>
'''
Variable scope determines where a variable is accessible.
1. Local scope - inside function
2. Global scope - at module level
3. Enclosing scope - outer functions
4. Built-in scope - Python built-in names
'''

# Example 17: Local vs Global variables
global_var = "I am global"

def demonstrate_scope():
    local_var = "I am local"
    print("Inside function - global_var:", global_var)  # Inside function - global_var: I am global
    print("Inside function - local_var:", local_var)    # Inside function - local_var: I am local

demonstrate_scope()
print("Outside function - global_var:", global_var)     # Outside function - global_var: I am global
# print(local_var)  # NameError: name 'local_var' is not defined

# Example 18: Modifying global variables
counter = 0

def increment_counter():
    global counter
    counter += 1
    return counter

print("Counter:", increment_counter())              # Counter: 1
print("Counter:", increment_counter())              # Counter: 2
print("Counter:", increment_counter())              # Counter: 3

# Example 19: Enclosing scope (nonlocal)
def outer():
    x = "outer variable"
    
    def inner():
        nonlocal x
        x = "modified by inner"
        print("Inner:", x)                         # Inner: modified by inner
    
    inner()
    print("Outer:", x)                             # Outer: modified by inner

outer()

# Example 20: Variable lifetime
def create_list():
    """Local list is created and destroyed after function execution"""
    temp_list = [1, 2, 3, 4, 5]
    return temp_list

result = create_list()
print("Result:", result)                           # Result: [1, 2, 3, 4, 5]
# temp_list no longer exists after function execution

## 7. Lambda Functions <a name="lambda-functions"></a>
'''
Lambda functions are small anonymous functions defined using lambda keyword.
Syntax: lambda arguments: expression
'''

# Example 21: Basic lambda functions
square = lambda x: x ** 2
print("Square of 5:", square(5))                   # Square of 5: 25

add = lambda a, b: a + b
print("Sum of 3 and 5:", add(3, 5))                # Sum of 3 and 5: 8

is_even = lambda x: x % 2 == 0
print("Is 4 even?", is_even(4))                    # Is 4 even? True

# Example 22: Lambda with built-in functions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() - apply function to each element
squared = list(map(lambda x: x ** 2, numbers))
print("Squared:", squared)                         # Squared: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# filter() - filter elements based on condition
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)                             # Evens: [2, 4, 6, 8, 10]

# sorted() - custom sorting
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78},
    {"name": "Diana", "grade": 95}
]
sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)
print("Top student:", sorted_students[0]["name"]) # Top student: Diana

# Example 23: Lambda in conditional expressions
max_func = lambda a, b: a if a > b else b
print("Max of 10 and 20:", max_func(10, 20))       # Max of 10 and 20: 20

# Example 24: Lambda with list comprehensions
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
sorted_pairs = sorted(pairs, key=lambda x: len(x[1]))
print("Sorted by word length:", sorted_pairs)      # Sorted by word length: [(1, 'one'), (2, 'two'), (4, 'four'), (3, 'three')]

## 8. Recursion <a name="recursion"></a>
'''
Recursion is when a function calls itself.
Must have base case to prevent infinite recursion.
'''

# Example 25: Factorial using recursion
def factorial(n):
    """Calculate factorial using recursion"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))             # Factorial of 5: 120
print("Factorial of 7:", factorial(7))             # Factorial of 7: 5040

# Example 26: Fibonacci sequence using recursion
def fibonacci(n):
    """Calculate nth Fibonacci number using recursion"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci(7):", fibonacci(7))               # Fibonacci(7): 13
print("Fibonacci(10):", fibonacci(10))             # Fibonacci(10): 55

# Example 27: Recursion with memoization
def fibonacci_memo(n, memo={}):
    """Fibonacci with memoization for better performance"""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print("Fibonacci(35):", fibonacci_memo(35))        # Fibonacci(35): 9227465

# Example 28: Directory tree traversal (recursive)
def print_directory_structure(path, indent=0):
    """Recursively print directory structure"""
    import os
    try:
        items = os.listdir(path)
        for item in items:
            print("  " * indent + "|-", item)
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                print_directory_structure(full_path, indent + 1)
    except PermissionError:
        print("  " * indent + "|- [Permission Denied]")

# print_directory_structure(".")  # Uncomment to test

# Example 29: Recursive binary search
def binary_search(arr, target, left, right):
    """Recursive binary search"""
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)

sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print("Index of 13:", binary_search(sorted_numbers, 13, 0, len(sorted_numbers) - 1))  # Index of 13: 6
print("Index of 20:", binary_search(sorted_numbers, 20, 0, len(sorted_numbers) - 1))  # Index of 20: -1

## 9. Decorators <a name="decorators"></a>
'''
Decorators are functions that modify the behavior of other functions.
They are used to add functionality to existing functions without modifying them.
'''

# Example 30: Simple decorator
def timer(func):
    """Decorator to measure function execution time"""
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
    return "Done"

print(slow_function())                             # slow_function took 1.000123 seconds
                                                   # Done

# Example 31: Decorator with parameters
def repeat(times):
    """Decorator factory - repeat function execution"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("Alice"))                          # ['Hello, Alice!', 'Hello, Alice!', 'Hello, Alice!']

# Example 32: Multiple decorators
def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclamation(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"
    return wrapper

@uppercase
@exclamation
def greet(name):
    return f"Hello, {name}"

print(greet("Bob"))                                # HELLO, BOB!

# Example 33: Class-based decorator
class CountCalls:
    """Decorator class to count function calls"""
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Function {self.func.__name__} called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    return "Hi!"

print(say_hi())                                    # Function say_hi called 1 times
                                                   # Hi!
print(say_hi())                                    # Function say_hi called 2 times
                                                   # Hi!

## 10. Generators <a name="generators"></a>
'''
Generators are functions that yield values one at a time.
They are memory efficient for large sequences.
'''

# Example 34: Simple generator
def count_up_to(n):
    """Generator that counts from 1 to n"""
    i = 1
    while i <= n:
        yield i
        i += 1

counter = count_up_to(5)
print(next(counter))                               # 1
print(next(counter))                               # 2
print(next(counter))                               # 3
print(next(counter))                               # 4
print(next(counter))                               # 5
# print(next(counter))  # StopIteration

# Example 35: Generator expression vs list comprehension
import sys

# List comprehension - creates entire list in memory
squares_list = [x**2 for x in range(1000000)]
print(f"List size: {sys.getsizeof(squares_list)} bytes")  # List size: 8448728 bytes

# Generator expression - yields one value at a time
squares_gen = (x**2 for x in range(1000000))
print(f"Generator size: {sys.getsizeof(squares_gen)} bytes")  # Generator size: 200 bytes

# Example 36: Fibonacci generator
def fibonacci_generator(limit):
    """Generate Fibonacci sequence up to limit"""
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

fib = fibonacci_generator(10)
print("First 10 Fibonacci numbers:")
for num in fib:
    print(num, end=" ")                            # 0 1 1 2 3 5 8 13 21 34
print()

# Example 37: Infinite generator
def infinite_sequence():
    """Generate infinite sequence of numbers"""
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
print(next(gen))                                   # 0
print(next(gen))                                   # 1
print(next(gen))                                   # 2
print(next(gen))                                   # 3

# Example 38: Generator pipeline
def read_file_lines(filename):
    """Generator to read file lines one by one"""
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

def filter_lines(lines, keyword):
    """Generator to filter lines containing keyword"""
    for line in lines:
        if keyword in line:
            yield line

def count_words(lines):
    """Generator to count words in each line"""
    for line in lines:
        yield len(line.split())

# Pipeline: read -> filter -> count
# lines = read_file_lines("sample.txt")
# filtered = filter_lines(lines, "Python")
# word_counts = count_words(filtered)
# for count in word_counts:
#     print(count)

## 11. Built-in Functions <a name="built-in-functions"></a>
'''
Python has many built-in functions for common operations.
'''

# Example 39: Math functions
print("abs(-5):", abs(-5))                         # abs(-5): 5
print("divmod(10,3):", divmod(10, 3))              # divmod(10,3): (3, 1)
print("pow(2,3):", pow(2, 3))                     # pow(2,3): 8
print("round(3.14159,2):", round(3.14159, 2))      # round(3.14159,2): 3.14
print("sum([1,2,3,4,5]):", sum([1, 2, 3, 4, 5]))   # sum([1,2,3,4,5]): 15

# Example 40: Type conversion functions
print("int('42'):", int("42"))                     # int('42'): 42
print("float('3.14'):", float("3.14"))             # float('3.14'): 3.14
print("str(100):", str(100))                       # str(100): '100'
print("list('hello'):", list("hello"))             # list('hello'): ['h', 'e', 'l', 'l', 'o']
print("tuple([1,2,3]):", tuple([1, 2, 3]))         # tuple([1,2,3]): (1, 2, 3)
print("set([1,2,2,3,3,3]):", set([1, 2, 2, 3, 3, 3])) # set([1,2,2,3,3,3]): {1, 2, 3}

# Example 41: Iterable functions
numbers = [1, 2, 3, 4, 5]

print("len(numbers):", len(numbers))               # len(numbers): 5
print("max(numbers):", max(numbers))               # max(numbers): 5
print("min(numbers):", min(numbers))               # min(numbers): 1
print("enumerate(numbers):", list(enumerate(numbers))) # enumerate(numbers): [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print("zip([1,2,3], ['a','b','c']):", list(zip([1, 2, 3], ['a', 'b', 'c']))) # zip(...): [(1, 'a'), (2, 'b'), (3, 'c')]

# Example 42: Object inspection functions
print("type(42):", type(42))                       # type(42): <class 'int'>
print("isinstance(42, int):", isinstance(42, int)) # isinstance(42, int): True
print("callable(len):", callable(len))             # callable(len): True
print("dir(list):", dir(list)[:5])                 # dir(list): ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', ...]
print("help(len):", "Use help(len) in interactive mode")

## 12. Practical Examples <a name="practical-examples"></a>
'''
Real-world applications of functions
'''

# Example 43: Calculator using functions
def calculator():
    """Simple calculator using functions"""
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        if b != 0:
            return a / b
        return "Cannot divide by zero"
    
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    
    return operations

calc_ops = calculator()
print("5 + 3 =", calc_ops['+'](5, 3))              # 5 + 3 = 8
print("10 - 4 =", calc_ops['-'](10, 4))            # 10 - 4 = 6
print("6 * 7 =", calc_ops['*'](6, 7))              # 6 * 7 = 42
print("15 / 3 =", calc_ops['/'](15, 3))            # 15 / 3 = 5.0

# Example 44: Data validation functions
def create_validator():
    """Create data validation functions"""
    
    def validate_email(email):
        """Validate email format"""
        return '@' in email and '.' in email
    
    def validate_age(age):
        """Validate age is between 0 and 150"""
        try:
            age = int(age)
            return 0 <= age <= 150
        except ValueError:
            return False
    
    def validate_phone(phone):
        """Validate phone number format"""
        import re
        pattern = r'^\+?1?\d{9,15}$'
        return bool(re.match(pattern, phone))
    
    return {
        'email': validate_email,
        'age': validate_age,
        'phone': validate_phone
    }

validator = create_validator()
print("Valid email 'test@email.com':", validator['email']("test@email.com"))  # Valid email 'test@email.com': True
print("Valid age '25':", validator['age']("25"))                             # Valid age '25': True
print("Valid phone '+1234567890':", validator['phone']("+1234567890"))       # Valid phone '+1234567890': True

# Example 45: File processing functions
def file_processor(filename):
    """Functions to process files"""
    
    def count_lines():
        """Count lines in file"""
        try:
            with open(filename, 'r') as f:
                return len(f.readlines())
        except FileNotFoundError:
            return 0
    
    def count_words():
        """Count words in file"""
        try:
            with open(filename, 'r') as f:
                content = f.read()
                return len(content.split())
        except FileNotFoundError:
            return 0
    
    def count_characters():
        """Count characters in file"""
        try:
            with open(filename, 'r') as f:
                content = f.read()
                return len(content)
        except FileNotFoundError:
            return 0
    
    return {
        'lines': count_lines,
        'words': count_words,
        'characters': count_characters
    }

# processor = file_processor("sample.txt")
# print("Lines:", processor['lines']())
# print("Words:", processor['words']())
# print("Characters:", processor['characters']())

# Example 46: Caching/Memoization decorator
def memoize(func):
    """Generic memoization decorator"""
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for {args}")
            return cache[args]
        print(f"Cache miss for {args}")
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci_cached(n):
    """Fibonacci with memoization decorator"""
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)

print("Fib(10):", fibonacci_cached(10))            # Cache miss for (10,) ... etc
                                                   # Fib(10): 55
print("Fib(10) again:", fibonacci_cached(10))      # Cache hit for (10,)
                                                   # Fib(10) again: 55

# Example 47: Function to validate and sanitize data
def create_data_processor():
    """Create data processing pipeline"""
    
    def sanitize_string(text):
        """Remove extra whitespace and convert to lowercase"""
        return ' '.join(text.strip().lower().split())
    
    def validate_numeric(value):
        """Check if value is numeric"""
        try:
            float(value)
            return True
        except ValueError:
            return False
    
    def process_person_data(data):
        """Process person dictionary"""
        processed = {}
        
        # Sanitize name
        if 'name' in data:
            processed['name'] = sanitize_string(data['name'])
        
        # Validate age
        if 'age' in data and validate_numeric(data['age']):
            processed['age'] = int(data['age'])
        
        # Process email
        if 'email' in data:
            processed['email'] = data['email'].lower().strip()
        
        return processed
    
    return process_person_data

processor = create_data_processor()
raw_data = {
    'name': '  ALICE SMITH  ',
    'age': '25',
    'email': 'Alice.Smith@EMAIL.COM'
}
processed = processor(raw_data)
print("Processed data:", processed)                 # Processed data: {'name': 'alice smith', 'age': 25, 'email': 'alice.smith@email.com'}

# Example 48: Function to calculate statistics
def create_statistics_calculator():
    """Create functions for statistical calculations"""
    
    def mean(data):
        """Calculate mean"""
        return sum(data) / len(data) if data else 0
    
    def median(data):
        """Calculate median"""
        if not data:
            return 0
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]
    
    def mode(data):
        """Calculate mode"""
        from collections import Counter
        if not data:
            return None
        counter = Counter(data)
        max_count = max(counter.values())
        modes = [k for k, v in counter.items() if v == max_count]
        return modes[0] if len(modes) == 1 else modes
    
    def std_dev(data):
        """Calculate standard deviation"""
        if len(data) < 2:
            return 0
        avg = mean(data)
        variance = sum((x - avg) ** 2 for x in data) / (len(data) - 1)
        return variance ** 0.5
    
    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'std_dev': std_dev
    }

stats = create_statistics_calculator()
data = [2, 3, 4, 4, 5, 5, 5, 6, 7, 8]
print("Mean:", stats['mean'](data))                # Mean: 4.9
print("Median:", stats['median'](data))            # Median: 5.0
print("Mode:", stats['mode'](data))                # Mode: 5
print("Standard deviation:", stats['std_dev'](data)) # Standard deviation: 1.852925754666222

# Example 49: URL parameter parser
def parse_query_string():
    """Parse URL query string into dictionary"""
    
    def parse(query_string):
        """Convert query string to dictionary"""
        if not query_string:
            return {}
        
        params = {}
        pairs = query_string.split('&')
        
        for pair in pairs:
            if '=' in pair:
                key, value = pair.split('=', 1)
                params[key] = value
        
        return params
    
    def build(params):
        """Convert dictionary to query string"""
        if not params:
            return ""
        
        pairs = []
        for key, value in params.items():
            pairs.append(f"{key}={value}")
        
        return "&".join(pairs)
    
    return {'parse': parse, 'build': build}

url_parser = parse_query_string()
query = "name=Alice&age=25&city=NYC&active=true"
parsed = url_parser['parse'](query)
print("Parsed URL:", parsed)                       # Parsed URL: {'name': 'Alice', 'age': '25', 'city': 'NYC', 'active': 'true'}

built_query = url_parser['build'](parsed)
print("Built query:", built_query)                 # Built query: name=Alice&age=25&city=NYC&active=true

# Example 50: Function composition
def compose(*functions):
    """Compose multiple functions together"""
    def composed_function(arg):
        result = arg
        for func in reversed(functions):
            result = func(result)
        return result
    return composed_function

def double(x):
    return x * 2

def add_one(x):
    return x + 1

def square(x):
    return x ** 2

# Compose functions
double_then_square = compose(square, double)
print("double_then_square(5):", double_then_square(5))  # double_then_square(5): 100

add_one_then_double = compose(double, add_one)
print("add_one_then_double(5):", add_one_then_double(5))  # add_one_then_double(5): 12

# Chain multiple functions
process = compose(square, double, add_one)
print("square(double(add_one(5))):", process(5))    # square(double(add_one(5))): 144

## 13. Function Best Practices

# Example 51: Docstrings and type hints (Python 3.5+)
def calculate_discount(price: float, discount_percent: float = 10.0) -> float:
    """
    Calculate discounted price.
    
    Args:
        price (float): Original price
        discount_percent (float): Discount percentage (default: 10.0)
    
    Returns:
        float: Discounted price
    
    Raises:
        ValueError: If price or discount_percent is negative
    
    Examples:
        >>> calculate_discount(100.0, 20.0)
        80.0
        >>> calculate_discount(50.0)
        45.0
    """
    if price < 0 or discount_percent < 0:
        raise ValueError("Price and discount must be non-negative")
    
    discount = price * (discount_percent / 100)
    return round(price - discount, 2)

print(calculate_discount(100, 20))                 # 80.0
print(calculate_discount(49.99))                   # 44.99
print(calculate_discount.__doc__)                  # Calculate discounted price...

# Example 52: Error handling in functions
def safe_divide(a, b):
    """Safely divide two numbers with error handling"""
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except TypeError:
        print("Error: Invalid operand type!")
        return None
    else:
        return result
    finally:
        print(f"Attempted to divide {a} by {b}")

print("Result:", safe_divide(10, 2))               # Attempted to divide 10 by 2
                                                   # Result: 5.0
print("Result:", safe_divide(10, 0))               # Error: Division by zero!
                                                   # Attempted to divide 10 by 0
                                                   # Result: None

# Example 53: Function with default mutable argument (caution!)
def add_item(item, items=[]):
    """BAD: Default mutable argument"""
    items.append(item)
    return items

def add_item_correct(item, items=None):
    """GOOD: Use None as default for mutable arguments"""
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))                                 # [1]
print(add_item(2))                                 # [1, 2]  (shared list!)
print(add_item_correct(1))                         # [1]
print(add_item_correct(2))                         # [2]  (new list each time)

# Example 54: Function factory
def create_multiplier(factor):
    """Create a function that multiplies by given factor"""
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

print("Double 5:", double(5))                      # Double 5: 10
print("Triple 5:", triple(5))                     # Triple 5: 15
print("Quadruple 5:", quadruple(5))               # Quadruple 5: 20

## 14. Function Summary

'''
Functions are fundamental building blocks in Python:

KEY CONCEPTS:
------------
1. Definition: def function_name(parameters):
2. Calling: function_name(arguments)
3. Parameters: positional, keyword, default, *args, **kwargs
4. Return: returns value (None if no return)
5. Scope: local, global, nonlocal, built-in
6. Types: regular, lambda, inner, recursive, generator
7. Decorators: modify function behavior
8. Generators: yield values one at a time

BEST PRACTICES:
--------------
1. Use descriptive function names
2. Write docstrings for documentation
3. Keep functions small and focused
4. Use type hints for clarity
5. Avoid modifying mutable arguments
6. Handle exceptions appropriately
7. Use default parameters wisely
8. Follow single responsibility principle

COMMON USE CASES:
----------------
1. Code reuse and organization
2. Mathematical calculations
3. Data processing and validation
4. File operations
5. API integrations
6. Algorithm implementation
7. Event handling
8. State management
'''