# Python Dictionaries Documentation

## Table of Contents
# 1. [Introduction to Dictionaries](#introduction)
# 2. [Dictionary Creation](#creation)
# 3. [Dictionary Access & Modification](#access-modification)
# 4. [Dictionary Methods](#methods)
# 5. [Dictionary Operations](#operations)
# 6. [Dictionary Comprehensions](#comprehensions)
# 7. [Nested Dictionaries](#nested-dictionaries)
# 8. [Dictionary vs Other Data Types](#vs-other)
# 9. [Ordered Dictionaries](#ordered-dicts)
# 10. [Practical Examples](#practical-examples)


## 1. Introduction to Dictionaries <a name="introduction"></a>
'''
Dictionaries are unordered collections of key-value pairs in Python.
They are mutable, indexed by keys (not by position), and very efficient for lookups.
Keys must be immutable and unique, while values can be of any type.
'''

'''
Key Characteristics:
- Unordered (Python 3.6+ maintains insertion order)
- Key-Value pairs
- Keys must be immutable and unique
- Values can be any data type
- Mutable (can be modified)
- Very fast lookups (O(1) average)
'''

# Example 1: Basic dictionary
student = {
    "name": "John Doe",
    "age": 20,
    "course": "Computer Science",
    "gpa": 3.8
}
print(type(student))                                 # <class 'dict'>
print(student)                                       # {'name': 'John Doe', 'age': 20, 'course': 'Computer Science', 'gpa': 3.8}

## 2. Dictionary Creation <a name="creation"></a>
'''
There are multiple ways to create dictionaries:
1. Using curly braces {}
2. Using dict() constructor
3. From sequence of key-value pairs
4. Using dictionary comprehensions
'''

# Example 2: Different ways to create dictionaries
# Using curly braces
empty_dict = {}  # Empty dictionary
person = {"name": "Alice", "age": 25, "city": "NYC"}

# Using dict() constructor
dict1 = dict(name="Bob", age=30, city="LA")  # Keyword arguments
dict2 = dict([("name", "Charlie"), ("age", 35), ("city", "Chicago")])  # List of tuples
dict3 = dict(zip(["name", "age", "city"], ["David", 40, "Boston"]))  # Using zip

# Using fromkeys() method
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys)  # All values set to None
default_dict_value = dict.fromkeys(keys, 0)  # All values set to 0

print("Empty dict:", empty_dict)                    # Empty dict: {}
print("Person dict:", person)                       # Person dict: {'name': 'Alice', 'age': 25, 'city': 'NYC'}
print("Dict from keywords:", dict1)                 # Dict from keywords: {'name': 'Bob', 'age': 30, 'city': 'LA'}
print("Dict from list of tuples:", dict2)           # Dict from list of tuples: {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
print("Dict from zip:", dict3)                      # Dict from zip: {'name': 'David', 'age': 40, 'city': 'Boston'}
print("Default dict:", default_dict)                # Default dict: {'a': None, 'b': None, 'c': None}
print("Default dict with value 0:", default_dict_value) # Default dict with value 0: {'a': 0, 'b': 0, 'c': 0}

# Example 3: Valid and invalid keys
valid_dict = {
    1: "integer key",
    3.14: "float key",
    "name": "string key",
    (1, 2, 3): "tuple key",  # Tuple is immutable
    True: "boolean key",
    None: "None key"
}
print("Dictionary with various key types:", valid_dict) # Dictionary with various key types: {1: 'integer key', 3.14: 'float key', 'name': 'string key', (1, 2, 3): 'tuple key', True: 'boolean key', None: 'None key'}

# Invalid keys (mutable types)
# invalid_dict = {
#     [1, 2]: "list key"  # TypeError: unhashable type: 'list'
# }
# invalid_dict = {
#     {1, 2}: "set key"  # TypeError: unhashable type: 'set'
# }

## 3. Dictionary Access & Modification <a name="access-modification"></a>
'''
Dictionaries can be accessed and modified using keys.
Various methods exist for safe access and modification.
'''

# Example 4: Accessing dictionary elements
employee = {
    "id": 101,
    "name": "Alice Smith",
    "position": "Software Engineer",
    "salary": 75000,
    "skills": ["Python", "Java", "SQL"]
}

# Access using square brackets
print("Name:", employee["name"])                    # Name: Alice Smith
print("Position:", employee["position"])            # Position: Software Engineer
print("Skills:", employee["skills"])                # Skills: ['Python', 'Java', 'SQL']

# Access using get() method (safer)
print("Salary using get():", employee.get("salary")) # Salary using get(): 75000
print("Department using get():", employee.get("department")) # Department using get(): None
print("Department with default:", employee.get("department", "Not specified")) # Department with default: Not specified

# Example 5: Modifying dictionaries
# Adding new key-value pair
employee["department"] = "Engineering"
print("After adding department:", employee)         # After adding department: {'id': 101, 'name': 'Alice Smith', 'position': 'Software Engineer', 'salary': 75000, 'skills': ['Python', 'Java', 'SQL'], 'department': 'Engineering'}

# Modifying existing value
employee["salary"] = 80000
print("After salary update:", employee["salary"])   # After salary update: 80000

# Adding to list value
employee["skills"].append("JavaScript")
print("After adding skill:", employee["skills"])    # After adding skill: ['Python', 'Java', 'SQL', 'JavaScript']

# Example 6: Deleting elements
# Using del keyword
del employee["department"]
print("After deleting department:", employee)       # After deleting department: {'id': 101, 'name': 'Alice Smith', 'position': 'Software Engineer', 'salary': 80000, 'skills': ['Python', 'Java', 'SQL', 'JavaScript']}

# Using pop() method
removed_salary = employee.pop("salary")
print(f"Removed salary: {removed_salary}")          # Removed salary: 80000
print("After popping salary:", employee)            # After popping salary: {'id': 101, 'name': 'Alice Smith', 'position': 'Software Engineer', 'skills': ['Python', 'Java', 'SQL', 'JavaScript']}

# Using popitem() (removes last inserted item in Python 3.7+)
last_item = employee.popitem()
print(f"Last item removed: {last_item}")            # Last item removed: ('skills', ['Python', 'Java', 'SQL', 'JavaScript'])
print("After popitem():", employee)                 # After popitem(): {'id': 101, 'name': 'Alice Smith', 'position': 'Software Engineer'}

# Using clear() method
employee_copy = employee.copy()
employee_copy.clear()
print("After clear():", employee_copy)              # After clear(): {}

## 4. Dictionary Methods <a name="methods"></a>
'''
Dictionary methods can be categorized as:
1. Access methods
2. Modification methods
3. View methods (keys, values, items)
4. Update and copy methods
'''

# Example 7: Access methods
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
    "max_connections": 100
}

# keys() - returns view of all keys
print("Keys:", config.keys())                       # Keys: dict_keys(['host', 'port', 'debug', 'max_connections'])

# values() - returns view of all values
print("Values:", config.values())                   # Values: dict_values(['localhost', 8080, True, 100])

# items() - returns view of all key-value pairs as tuples
print("Items:", config.items())                     # Items: dict_items([('host', 'localhost'), ('port', 8080), ('debug', True), ('max_connections', 100)])

# Example 8: Using dictionary views
for key in config.keys():
    print(f"Key: {key}")                            # Key: host
                                                    # Key: port
                                                    # Key: debug
                                                    # Key: max_connections

for value in config.values():
    print(f"Value: {value}")                        # Value: localhost
                                                    # Value: 8080
                                                    # Value: True
                                                    # Value: 100

for key, value in config.items():
    print(f"{key}: {value}")                        # host: localhost
                                                    # port: 8080
                                                    # debug: True
                                                    # max_connections: 100

# Example 9: Update methods
dict_a = {"a": 1, "b": 2}
dict_b = {"b": 3, "c": 4, "d": 5}

# update() - merges dictionaries
dict_a.update(dict_b)
print("After update:", dict_a)                      # After update: {'a': 1, 'b': 3, 'c': 4, 'd': 5}

# setdefault() - gets value if key exists, sets default if not
car = {"brand": "Toyota", "model": "Camry", "year": 2020}

color = car.setdefault("color", "White")
print(f"Color: {color}")                            # Color: White
print("Car dict:", car)                             # Car dict: {'brand': 'Toyota', 'model': 'Camry', 'year': 2020, 'color': 'White'}

existing = car.setdefault("model", "Corolla")
print(f"Existing model: {existing}")                # Existing model: Camry

# Example 10: Copy method
original = {"name": "Alice", "age": 25, "hobbies": ["reading", "swimming"]}

# Shallow copy
shallow_copy = original.copy()
shallow_copy["age"] = 26
shallow_copy["hobbies"].append("coding")

print("Original:", original)                        # Original: {'name': 'Alice', 'age': 25, 'hobbies': ['reading', 'swimming', 'coding']}
print("Shallow copy:", shallow_copy)                # Shallow copy: {'name': 'Alice', 'age': 26, 'hobbies': ['reading', 'swimming', 'coding']}

# Deep copy (for nested mutable objects)
import copy
deep_copy = copy.deepcopy(original)
deep_copy["hobbies"].append("painting")
print("Original after deep copy:", original)        # Original after deep copy: {'name': 'Alice', 'age': 25, 'hobbies': ['reading', 'swimming', 'coding']}
print("Deep copy:", deep_copy)                      # Deep copy: {'name': 'Alice', 'age': 25, 'hobbies': ['reading', 'swimming', 'coding', 'painting']}

## 5. Dictionary Operations <a name="operations"></a>
'''
Dictionary operations include:
1. Membership testing (in, not in)
2. Length calculation
3. Merging dictionaries
4. Dictionary comparisons
'''

# Example 11: Membership testing
inventory = {
    "apple": 50,
    "banana": 30,
    "orange": 40,
    "grape": 25
}

print("'apple' in inventory:", "apple" in inventory) # 'apple' in inventory: True
print("'mango' not in inventory:", "mango" not in inventory) # 'mango' not in inventory: True
print("50 in inventory.values():", 50 in inventory.values()) # 50 in inventory.values(): True

# Example 12: Length and other operations
print("Length of inventory:", len(inventory))       # Length of inventory: 4

# Dictionary merging (Python 3.5+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}

# Using unpacking ** operator
merged = {**dict1, **dict2, **dict3}
print("Merged dictionary:", merged)                 # Merged dictionary: {'a': 1, 'b': 3, 'c': 4, 'd': 5}

# Using | operator (Python 3.9+)
# merged = dict1 | dict2 | dict3

# Example 13: Dictionary comparisons
dict_a = {"x": 1, "y": 2}
dict_b = {"x": 1, "y": 2}
dict_c = {"x": 1, "y": 3}

print("dict_a == dict_b:", dict_a == dict_b)        # dict_a == dict_b: True
print("dict_a == dict_c:", dict_a == dict_c)        # dict_a == dict_c: False
print("dict_a != dict_c:", dict_a != dict_c)        # dict_a != dict_c: True

## 6. Dictionary Comprehensions <a name="comprehensions"></a>
'''
Dictionary comprehensions provide a concise way to create dictionaries.
Syntax: {key_expression: value_expression for item in iterable if condition}
'''

# Example 14: Basic dictionary comprehensions
# Squares of numbers
squares = {x: x**2 for x in range(1, 6)}
print("Squares:", squares)                          # Squares: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Uppercase mapping
fruits = ["apple", "banana", "cherry"]
upper_fruits = {fruit: fruit.upper() for fruit in fruits}
print("Uppercase fruits:", upper_fruits)            # Uppercase fruits: {'apple': 'APPLE', 'banana': 'BANANA', 'cherry': 'CHERRY'}

# Filtering with condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = {n: n**2 for n in numbers if n % 2 == 0}
print("Even squares:", even_squares)                # Even squares: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Example 15: Swapping keys and values
original = {"a": 1, "b": 2, "c": 3, "d": 4}
swapped = {value: key for key, value in original.items()}
print("Swapped dictionary:", swapped)               # Swapped dictionary: {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# Example 16: Dictionary comprehension with conditional value
temperatures = {"Delhi": 35, "Mumbai": 32, "Chennai": 38, "Bangalore": 28}
status = {city: "Hot" if temp > 30 else "Cool" for city, temp in temperatures.items()}
print("Temperature status:", status)                # Temperature status: {'Delhi': 'Hot', 'Mumbai': 'Hot', 'Chennai': 'Hot', 'Bangalore': 'Cool'}

# Example 17: Nested dictionary comprehension
# Multiplication table
table = {i: {j: i*j for j in range(1, 6)} for i in range(1, 4)}
print("Multiplication table:", table)               # Multiplication table: {1: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}, 2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}, 3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15}}

## 7. Nested Dictionaries <a name="nested-dictionaries"></a>
'''
Dictionaries can contain other dictionaries as values.
This is useful for representing hierarchical or complex data structures.
'''

# Example 18: Nested dictionaries
company = {
    "employee1": {
        "name": "Alice",
        "age": 28,
        "position": "Manager",
        "salary": 60000
    },
    "employee2": {
        "name": "Bob",
        "age": 32,
        "position": "Developer",
        "salary": 55000
    },
    "employee3": {
        "name": "Charlie",
        "age": 25,
        "position": "Designer",
        "salary": 50000
    }
}

print("Company structure:", company)                # Company structure: {'employee1': {'name': 'Alice', 'age': 28, 'position': 'Manager', 'salary': 60000}, 'employee2': {'name': 'Bob', 'age': 32, 'position': 'Developer', 'salary': 55000}, 'employee3': {'name': 'Charlie', 'age': 25, 'position': 'Designer', 'salary': 50000}}

# Accessing nested values
print("Employee2 name:", company["employee2"]["name"]) # Employee2 name: Bob
print("Employee3 salary:", company["employee3"]["salary"]) # Employee3 salary: 50000

# Modifying nested dictionary
company["employee1"]["salary"] = 65000
company["employee2"]["position"] = "Senior Developer"
print("After modifications:", company)              # After modifications: {'employee1': {'name': 'Alice', 'age': 28, 'position': 'Manager', 'salary': 65000}, 'employee2': {'name': 'Bob', 'age': 32, 'position': 'Senior Developer', 'salary': 55000}, 'employee3': {'name': 'Charlie', 'age': 25, 'position': 'Designer', 'salary': 50000}}

# Example 19: Complex nested structure
school = {
    "school_name": "ABC Public School",
    "principal": "Dr. Smith",
    "classes": {
        "10th": {
            "class_teacher": "Mr. Johnson",
            "students": 40,
            "subjects": ["Math", "Science", "English", "History"]
        },
        "11th": {
            "class_teacher": "Ms. Davis",
            "students": 35,
            "subjects": ["Physics", "Chemistry", "Biology", "Math"]
        },
        "12th": {
            "class_teacher": "Mr. Wilson",
            "students": 38,
            "subjects": ["Computer Science", "Economics", "Accounts", "Business"]
        }
    }
}

# Accessing deeply nested values
print("10th class teacher:", school["classes"]["10th"]["class_teacher"]) # 10th class teacher: Mr. Johnson
print("11th class subjects:", school["classes"]["11th"]["subjects"]) # 11th class subjects: ['Physics', 'Chemistry', 'Biology', 'Math']

# Adding new class
school["classes"]["9th"] = {
    "class_teacher": "Mrs. Taylor",
    "students": 42,
    "subjects": ["Math", "Science", "English", "Social Studies"]
}
print("After adding 9th class:", school["classes"].keys()) # After adding 9th class: dict_keys(['10th', '11th', '12th', '9th'])

## 8. Dictionary vs Other Data Types <a name="vs-other"></a>
'''
Comparison of dictionaries with lists, tuples, and sets
'''

# Example 20: Dictionary vs List
# List (ordered, indexed by position)
student_list = ["Alice", 20, "Computer Science", 3.8]
print("List - Name:", student_list[0])              # List - Name: Alice

# Dictionary (unordered, indexed by keys)
student_dict = {"name": "Alice", "age": 20, "course": "Computer Science", "gpa": 3.8}
print("Dict - Name:", student_dict["name"])         # Dict - Name: Alice

# Converting between list of tuples and dictionary
pairs = [("a", 1), ("b", 2), ("c", 3)]
list_to_dict = dict(pairs)
print("List of tuples to dict:", list_to_dict)      # List of tuples to dict: {'a': 1, 'b': 2, 'c': 3}

# Dictionary to list of tuples
dict_to_list = list(student_dict.items())
print("Dict to list of tuples:", dict_to_list)      # Dict to list of tuples: [('name', 'Alice'), ('age', 20), ('course', 'Computer Science'), ('gpa', 3.8)]

# Example 21: Performance comparison
import time

# Large dictionary vs list lookup
large_dict = {i: i*2 for i in range(1000000)}
large_list = [i for i in range(1000000)]

# Dictionary lookup (O(1) average)
start = time.time()
_ = 999999 in large_dict
dict_time = time.time() - start

# List lookup (O(n))
start = time.time()
_ = 999999 in large_list
list_time = time.time() - start

print(f"Dictionary lookup time: {dict_time:.6f} seconds")   # Dictionary lookup time: 0.000012 seconds
print(f"List lookup time: {list_time:.6f} seconds")         # List lookup time: 0.009876 seconds
print(f"Dictionary is {list_time/dict_time:.0f}x faster")   # Dictionary is 823x faster

## 9. Ordered Dictionaries <a name="ordered-dicts"></a>
'''
OrderedDict maintains insertion order (Python 3.7+ regular dict also does)
Useful when you need to maintain order or reorder items
'''

# Example 22: OrderedDict
from collections import OrderedDict

# Creating OrderedDict
ordered = OrderedDict()
ordered["z"] = 1
ordered["y"] = 2
ordered["x"] = 3
ordered["w"] = 4

print("OrderedDict:", ordered)                      # OrderedDict: OrderedDict([('z', 1), ('y', 2), ('x', 3), ('w', 4)])

# OrderedDict maintains insertion order
for key, value in ordered.items():
    print(f"{key}: {value}")                        # z: 1
                                                    # y: 2
                                                    # x: 3
                                                    # w: 4

# Moving items to end
ordered.move_to_end("z")
print("After moving 'z' to end:", ordered)          # After moving 'z' to end: OrderedDict([('y', 2), ('x', 3), ('w', 4), ('z', 1)])

# Moving items to beginning
ordered.move_to_end("z", last=False)
print("After moving 'z' to beginning:", ordered)    # After moving 'z' to beginning: OrderedDict([('z', 1), ('y', 2), ('x', 3), ('w', 4)])

# Example 23: DefaultDict (auto-initializes missing keys)
from collections import defaultdict

# DefaultDict with int (default 0)
word_count = defaultdict(int)
sentence = "apple banana apple orange banana apple"

for word in sentence.split():
    word_count[word] += 1

print("Word count:", dict(word_count))              # Word count: {'apple': 3, 'banana': 2, 'orange': 1}

# DefaultDict with list
student_grades = defaultdict(list)
grades_data = [("Alice", 85), ("Bob", 92), ("Alice", 90), ("Charlie", 78), ("Bob", 88)]

for student, grade in grades_data:
    student_grades[student].append(grade)

print("Student grades:", dict(student_grades))      # Student grades: {'Alice': [85, 90], 'Bob': [92, 88], 'Charlie': [78]}

# Example 24: Counter (specialized dictionary for counting)
from collections import Counter

# Counting elements
colors = ["red", "blue", "red", "green", "blue", "blue", "red"]
color_count = Counter(colors)
print("Color count:", color_count)                  # Color count: Counter({'red': 3, 'blue': 3, 'green': 1})

# Most common elements
print("Most common:", color_count.most_common(2))   # Most common: [('red', 3), ('blue', 3)]

# Counting characters in string
text = "mississippi"
char_count = Counter(text)
print("Character count:", char_count)               # Character count: Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

## 10. Practical Examples <a name="practical-examples"></a>
'''
Real-world applications of dictionaries
'''

# Example 25: Student Management System
students = {
    101: {"name": "Alice", "age": 20, "courses": ["Math", "Physics"], "gpa": 3.8},
    102: {"name": "Bob", "age": 21, "courses": ["Chemistry", "Biology"], "gpa": 3.5},
    103: {"name": "Charlie", "age": 19, "courses": ["Computer Science", "Math"], "gpa": 3.9},
    104: {"name": "Diana", "age": 20, "courses": ["Physics", "Chemistry"], "gpa": 3.7}
}

# Function to get student info
def get_student_info(student_id):
    student = students.get(student_id)
    if student:
        return f"Student {student_id}: {student['name']}, GPA: {student['gpa']}"
    else:
        return f"Student {student_id} not found"

print(get_student_info(101))                        # Student 101: Alice, GPA: 3.8
print(get_student_info(105))                        # Student 105 not found

# Function to add course to student
def add_course(student_id, course):
    if student_id in students:
        if course not in students[student_id]["courses"]:
            students[student_id]["courses"].append(course)
            return f"Course '{course}' added to {students[student_id]['name']}"
        else:
            return f"Course '{course}' already exists for {students[student_id]['name']}"
    else:
        return f"Student {student_id} not found"

print(add_course(101, "Chemistry"))                 # Course 'Chemistry' added to Alice
print(add_course(101, "Math"))                      # Course 'Math' already exists for Alice

# Example 26: Inventory Management System
inventory = {
    "electronics": {
        "laptop": {"price": 800, "quantity": 10},
        "smartphone": {"price": 500, "quantity": 25},
        "tablet": {"price": 300, "quantity": 15}
    },
    "clothing": {
        "tshirt": {"price": 20, "quantity": 100},
        "jeans": {"price": 50, "quantity": 75},
        "jacket": {"price": 80, "quantity": 40}
    },
    "books": {
        "python_book": {"price": 40, "quantity": 50},
        "novel": {"price": 15, "quantity": 200}
    }
}

# Function to check stock
def check_stock(category, product):
    return inventory.get(category, {}).get(product, {}).get("quantity", 0)

# Function to update stock
def update_stock(category, product, quantity_sold):
    if category in inventory and product in inventory[category]:
        current_qty = inventory[category][product]["quantity"]
        if current_qty >= quantity_sold:
            inventory[category][product]["quantity"] -= quantity_sold
            return f"Sold {quantity_sold} {product}(s). Remaining: {inventory[category][product]['quantity']}"
        else:
            return f"Insufficient stock. Available: {current_qty}"
    else:
        return "Product not found"

print("Laptop stock:", check_stock("electronics", "laptop")) # Laptop stock: 10
print(update_stock("electronics", "laptop", 3))              # Sold 3 laptop(s). Remaining: 7
print("Updated laptop stock:", check_stock("electronics", "laptop")) # Updated laptop stock: 7

# Example 27: Configuration Management
app_config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db",
        "user": "admin",
        "password": "secret123"
    },
    "server": {
        "host": "0.0.0.0",
        "port": 8080,
        "debug": True,
        "workers": 4
    },
    "logging": {
        "level": "INFO",
        "file": "app.log",
        "max_size": "10MB",
        "backup_count": 5
    }
}

# Function to get config with defaults
def get_config(section, key, default=None):
    return app_config.get(section, {}).get(key, default)

# Function to update config
def update_config(section, key, value):
    if section in app_config:
        app_config[section][key] = value
        return f"Updated {section}.{key} = {value}"
    else:
        return f"Section {section} not found"

print("Database host:", get_config("database", "host"))      # Database host: localhost
print("Cache timeout:", get_config("cache", "timeout", 60))   # Cache timeout: 60
print(update_config("server", "port", 9090))                 # Updated server.port = 9090

# Example 28: Word Frequency Counter
def word_frequency(text):
    """Count frequency of each word in text"""
    words = text.lower().split()
    frequency = {}
    
    for word in words:
        # Remove punctuation
        word = word.strip(".,!?;:\"()[]")
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    
    return frequency

sample_text = "Hello world! Hello Python. Python is awesome. World of Python."
freq = word_frequency(sample_text)

print("Word frequency:")
for word, count in sorted(freq.items()):
    print(f"  {word}: {count}")
'''
Word frequency:
  awesome: 1
  hello: 2
  is: 1
  of: 1
  python: 3
  world: 2
'''

# Example 29: Employee Database
employees = {}

def add_employee(emp_id, name, position, salary):
    employees[emp_id] = {
        "name": name,
        "position": position,
        "salary": salary,
        "projects": []
    }

def add_project(emp_id, project_name):
    if emp_id in employees:
        employees[emp_id]["projects"].append(project_name)
    else:
        print(f"Employee {emp_id} not found")

def get_employee_summary():
    summary = {}
    for emp_id, details in employees.items():
        summary[emp_id] = {
            "name": details["name"],
            "position": details["position"],
            "project_count": len(details["projects"])
        }
    return summary

# Add employees
add_employee(101, "Alice", "Manager", 60000)
add_employee(102, "Bob", "Developer", 50000)
add_employee(103, "Charlie", "Designer", 45000)

# Add projects
add_project(101, "Project Alpha")
add_project(101, "Project Beta")
add_project(102, "Project Gamma")
add_project(103, "Project Delta")

print("Employee summary:", get_employee_summary())  # Employee summary: {101: {'name': 'Alice', 'position': 'Manager', 'project_count': 2}, 102: {'name': 'Bob', 'position': 'Developer', 'project_count': 1}, 103: {'name': 'Charlie', 'position': 'Designer', 'project_count': 1}}

# Example 30: Dictionary for caching (Memoization)
def expensive_calculation(n, cache={}):
    """Calculate factorial with caching"""
    if n in cache:
        print(f"Cache hit for {n}!")
        return cache[n]
    
    print(f"Calculating factorial of {n}...")
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    cache[n] = result
    return result

# First time - calculation happens
print("Factorial 5:", expensive_calculation(5))     # Calculating factorial of 5...
                                                    # Factorial 5: 120

# Second time - from cache
print("Factorial 5 again:", expensive_calculation(5)) # Cache hit for 5!
                                                      # Factorial 5 again: 120

# New calculation
print("Factorial 7:", expensive_calculation(7))     # Calculating factorial of 7...
                                                    # Factorial 7: 5040