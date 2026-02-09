# Python Sets Documentation

## Table of Contents
# 1. [Introduction to Sets](#introduction)
# 2. [Set Creation](#creation)
# 3. [Set Operations](#operations)
# 4. [Set Methods](#methods)
# 5. [Set Comprehensions](#comprehensions)
# 6. [Frozen Sets](#frozen-sets)
# 7. [Set vs Other Data Types](#vs-other)
# 8. [Practical Examples](#practical-examples)

## 1. Introduction to Sets <a name="introduction"></a>
'''
Sets are unordered collections of unique elements in Python.
They are mutable but only contain immutable elements.
Sets are particularly useful for membership testing and eliminating duplicates.
'''

'''
Key Characteristics:
- Unordered (no indexing)
- Unique elements (no duplicates)
- Mutable (can add/remove elements)
- Contains only immutable elements
- Mathematical set operations supported
- Very fast membership testing (O(1))
'''

# Example 1: Basic sets
my_set = {1, 2, 3, 4, 5}
print(type(my_set))                                 # <class 'set'>
print(my_set)                                       # {1, 2, 3, 4, 5}

# Example 2: Sets remove duplicates automatically
duplicate_set = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
print(duplicate_set)                                # {1, 2, 3, 4}

## 2. Set Creation <a name="creation"></a>
'''
There are multiple ways to create sets in Python:
1. Using curly braces {}
2. Using set() constructor
3. From other iterables (lists, tuples, strings)
4. Using set comprehensions
'''

# Example 3: Different ways to create sets
# Using curly braces
empty_set = set()  # Note: {} creates empty dict, not set!
numbers_set = {1, 2, 3, 4, 5}
fruits_set = {"apple", "banana", "cherry"}

# Using set() constructor
from_list = set([1, 2, 3, 2, 1])
from_tuple = set((1, 2, 3, 2, 1))
from_string = set("hello")
from_range = set(range(5))

print("Empty set:", empty_set)                      # Empty set: set()
print("Numbers set:", numbers_set)                  # Numbers set: {1, 2, 3, 4, 5}
print("From list:", from_list)                      # From list: {1, 2, 3}
print("From tuple:", from_tuple)                    # From tuple: {1, 2, 3}
print("From string:", from_string)                  # From string: {'h', 'e', 'l', 'o'}
print("From range:", from_range)                    # From range: {0, 1, 2, 3, 4}

# Example 4: Sets with mixed types (but only immutable)
mixed_set = {1, 3.14, "hello", True, (1, 2, 3)}
print("Mixed set:", mixed_set)                      # Mixed set: {1, 3.14, 'hello', True, (1, 2, 3)}

# Example 5: Cannot have mutable elements in sets
# invalid_set = {1, [2, 3], 4}  # TypeError: unhashable type: 'list'
# invalid_set = {1, {2, 3}, 4}  # TypeError: unhashable type: 'set'

## 3. Set Operations <a name="operations"></a>
'''
Sets support mathematical set operations:
1. Union (| or union())
2. Intersection (& or intersection())
3. Difference (- or difference())
4. Symmetric Difference (^ or symmetric_difference())
'''

# Example 6: Set operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union (elements in A or B or both)
union_result = A | B
print("Union (A | B):", union_result)               # Union (A | B): {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection (elements in both A and B)
intersection_result = A & B
print("Intersection (A & B):", intersection_result) # Intersection (A & B): {4, 5}

# Difference (elements in A but not in B)
difference_result = A - B
print("Difference (A - B):", difference_result)     # Difference (A - B): {1, 2, 3}

# Symmetric Difference (elements in A or B but not both)
symmetric_diff = A ^ B
print("Symmetric Difference (A ^ B):", symmetric_diff) # Symmetric Difference (A ^ B): {1, 2, 3, 6, 7, 8}

# Example 7: Set comparison operations
C = {1, 2, 3}
D = {1, 2, 3, 4, 5}

print("C == {1, 2, 3}:", C == {1, 2, 3})            # C == {1, 2, 3}: True
print("C != {1, 2, 4}:", C != {1, 2, 4})            # C != {1, 2, 4}: True
print("C < D:", C < D)                              # C < D: True (proper subset)
print("C <= D:", C <= D)                            # C <= D: True (subset)
print("D > C:", D > C)                              # D > C: True (proper superset)
print("D >= C:", D >= C)                            # D >= C: True (superset)

# Example 8: Membership testing
colors = {"red", "green", "blue", "yellow", "purple"}
print("'red' in colors:", "red" in colors)          # 'red' in colors: True
print("'orange' not in colors:", "orange" not in colors) # 'orange' not in colors: True

# Example 9: Length and iteration
numbers = {10, 20, 30, 40, 50}
print("Length of numbers:", len(numbers))           # Length of numbers: 5

# Iterating through set (order not guaranteed)
for num in numbers:
    print(num, end=" ")                            # Output varies: 40 10 50 20 30
print()

## 4. Set Methods <a name="methods"></a>
'''
Set methods can be categorized as:
1. Adding/Removing elements
2. Set operations (mathematical)
3. Comparison operations
4. Other utility methods
'''

# Example 10: Adding elements
s = {1, 2, 3}

# add() - add single element
s.add(4)
print("After add(4):", s)                          # After add(4): {1, 2, 3, 4}

# update() - add multiple elements from iterable
s.update([5, 6, 7])
print("After update([5,6,7]):", s)                 # After update([5,6,7]): {1, 2, 3, 4, 5, 6, 7}

# Example 11: Removing elements
s = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# remove() - remove element, raises KeyError if not found
s.remove(5)
print("After remove(5):", s)                       # After remove(5): {1, 2, 3, 4, 6, 7, 8, 9}

# discard() - remove element, no error if not found
s.discard(10)  # No error even though 10 not in set
print("After discard(10):", s)                     # After discard(10): {1, 2, 3, 4, 6, 7, 8, 9}

# pop() - remove and return arbitrary element
removed = s.pop()
print(f"Popped element: {removed}")                # Popped element: 1 (arbitrary)
print("After pop():", s)                           # After pop(): {2, 3, 4, 6, 7, 8, 9}

# clear() - remove all elements
s.clear()
print("After clear():", s)                         # After clear(): set()

# Example 12: Set operation methods
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# union() method
union_set = A.union(B)
print("A.union(B):", union_set)                    # A.union(B): {1, 2, 3, 4, 5, 6, 7, 8}

# intersection() method
intersection_set = A.intersection(B)
print("A.intersection(B):", intersection_set)      # A.intersection(B): {4, 5}

# difference() method
difference_set = A.difference(B)
print("A.difference(B):", difference_set)          # A.difference(B): {1, 2, 3}

# symmetric_difference() method
sym_diff_set = A.symmetric_difference(B)
print("A.symmetric_difference(B):", sym_diff_set)  # A.symmetric_difference(B): {1, 2, 3, 6, 7, 8}

# Example 13: Update methods (modify in-place)
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# update() - union in-place
A_copy = A.copy()
A_copy.update(B)
print("After update (union):", A_copy)             # After update (union): {1, 2, 3, 4, 5, 6, 7, 8}

# intersection_update() - intersection in-place
A_copy = A.copy()
A_copy.intersection_update(B)
print("After intersection_update:", A_copy)        # After intersection_update: {4, 5}

# difference_update() - difference in-place
A_copy = A.copy()
A_copy.difference_update(B)
print("After difference_update:", A_copy)          # After difference_update: {1, 2, 3}

# symmetric_difference_update() - symmetric difference in-place
A_copy = A.copy()
A_copy.symmetric_difference_update(B)
print("After symmetric_difference_update:", A_copy) # After symmetric_difference_update: {1, 2, 3, 6, 7, 8}

# Example 14: Comparison methods
C = {1, 2, 3}
D = {1, 2, 3, 4, 5}
E = {4, 5, 6}

# isdisjoint() - no common elements
print("C.isdisjoint(D):", C.isdisjoint(D))         # C.isdisjoint(D): False
print("C.isdisjoint(E):", C.isdisjoint(E))         # C.isdisjoint(E): True

# issubset() - all elements of C in D
print("C.issubset(D):", C.issubset(D))             # C.issubset(D): True

# issuperset() - D contains all elements of C
print("D.issuperset(C):", D.issuperset(C))         # D.issuperset(C): True

# Example 15: Copy method
original = {1, 2, 3, 4, 5}
shallow_copy = original.copy()
shallow_copy.add(6)
print("Original:", original)                       # Original: {1, 2, 3, 4, 5}
print("Copy after add(6):", shallow_copy)          # Copy after add(6): {1, 2, 3, 4, 5, 6}

## 5. Set Comprehensions <a name="comprehensions"></a>
'''
Set comprehensions provide a concise way to create sets.
Syntax: {expression for item in iterable if condition}
'''

# Example 16: Set comprehensions
# Squares of numbers
squares = {x**2 for x in range(10)}
print("Squares:", squares)                         # Squares: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Even numbers
evens = {x for x in range(20) if x % 2 == 0}
print("Even numbers:", evens)                      # Even numbers: {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}

# Length of words
words = ["apple", "banana", "cherry", "date", "elderberry"]
word_lengths = {len(word) for word in words}
print("Word lengths:", word_lengths)               # Word lengths: {5, 6, 9}

# Remove vowels from string
text = "hello world"
no_vowels = {char for char in text if char not in 'aeiou '}
print("No vowels set:", no_vowels)                 # No vowels set: {'h', 'l', 'w', 'r', 'd'}

# Example 17: Nested set comprehension
# Cartesian product
A = {1, 2, 3}
B = {'a', 'b', 'c'}
cartesian = {(x, y) for x in A for y in B}
print("Cartesian product:", cartesian)             # Cartesian product: {(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')}

## 6. Frozen Sets <a name="frozen-sets"></a>
'''
Frozen sets are immutable sets.
They can be used as dictionary keys or elements of other sets.
'''

# Example 18: Frozen sets
# Creating frozen sets
frozen = frozenset([1, 2, 3, 4, 5])
print("Frozen set:", frozen)                       # Frozen set: frozenset({1, 2, 3, 4, 5})
print("Type:", type(frozen))                       # Type: <class 'frozenset'>

# Frozen sets are immutable
# frozen.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'
# frozen.remove(1)  # AttributeError

# Frozen sets can be dictionary keys
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([4, 5, 6])
frozen_dict = {fs1: "first", fs2: "second"}
print("Dictionary with frozen set keys:", frozen_dict) # Dictionary with frozen set keys: {frozenset({1, 2, 3}): 'first', frozenset({4, 5, 6}): 'second'}

# Frozen sets can be elements of other sets
set_of_frozen_sets = {frozenset([1, 2]), frozenset([3, 4]), frozenset([5, 6])}
print("Set of frozen sets:", set_of_frozen_sets)   # Set of frozen sets: {frozenset({5, 6}), frozenset({1, 2}), frozenset({3, 4})}

# Example 19: Frozen set operations
fs_a = frozenset([1, 2, 3, 4, 5])
fs_b = frozenset([4, 5, 6, 7, 8])

# Frozen sets support set operations (return new frozen sets)
print("Union:", fs_a | fs_b)                       # Union: frozenset({1, 2, 3, 4, 5, 6, 7, 8})
print("Intersection:", fs_a & fs_b)                # Intersection: frozenset({4, 5})
print("Difference:", fs_a - fs_b)                  # Difference: frozenset({1, 2, 3})
print("Symmetric difference:", fs_a ^ fs_b)        # Symmetric difference: frozenset({1, 2, 3, 6, 7, 8})

## 7. Set vs Other Data Types <a name="vs-other"></a>
'''
Sets vs Lists, Tuples, and Dictionaries
'''

# Example 20: Set vs List
# Removing duplicates from list
list_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_list = list(set(list_with_duplicates))
print("Original list:", list_with_duplicates)      # Original list: [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print("Unique elements:", unique_list)             # Unique elements: [1, 2, 3, 4]

# Example 21: Performance comparison - membership test
import time

large_list = list(range(1000000))
large_set = set(range(1000000))

# List membership test (O(n))
start = time.time()
999999 in large_list
list_time = time.time() - start

# Set membership test (O(1))
start = time.time()
999999 in large_set
set_time = time.time() - start

print(f"List membership test: {list_time:.6f} seconds")   # List membership test: 0.009876 seconds
print(f"Set membership test: {set_time:.6f} seconds")     # Set membership test: 0.000123 seconds
print(f"Set is {list_time/set_time:.0f}x faster")         # Set is 80x faster

# Example 22: Set vs Dictionary keys
# Both use hash tables for O(1) lookup
student_ids = {101, 102, 103, 104, 105}
student_dict = {101: "Alice", 102: "Bob", 103: "Charlie", 104: "Diana", 105: "Eve"}

print("Is 103 a valid ID?", 103 in student_ids)    # Is 103 a valid ID? True
print("Is 106 a valid ID?", 106 in student_ids)    # Is 106 a valid ID? False

## 8. Practical Examples <a name="practical-examples"></a>
'''
Real-world applications of sets
'''

# Example 23: Finding common elements between lists
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [2, 4, 6, 8, 10, 12, 14, 16, 18]

common_elements = set(list1) & set(list2)
print("Common elements:", common_elements)         # Common elements: {8, 2, 4, 6}

# Example 24: Removing stop words from text
stop_words = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to"}
text = "the quick brown fox jumps over the lazy dog and runs to the forest"

words = text.split()
filtered_words = [word for word in words if word not in stop_words]
print("Original text:", text)                      # Original text: the quick brown fox jumps over the lazy dog and runs to the forest
print("Filtered words:", filtered_words)           # Filtered words: ['quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog', 'runs', 'forest']

# Example 25: Finding unique characters in strings
string1 = "hello world"
string2 = "python programming"

unique_chars1 = set(string1)
unique_chars2 = set(string2)
common_chars = unique_chars1 & unique_chars2

print("Unique chars in 'hello world':", unique_chars1) # Unique chars in 'hello world': {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}
print("Unique chars in 'python programming':", unique_chars2) # Unique chars in 'python programming': {'p', 'y', 't', 'h', 'o', 'n', ' ', 'r', 'g', 'a', 'm', 'i'}
print("Common characters:", common_chars)          # Common characters: {'h', 'o', ' ', 'r'}

# Example 26: Course enrollment system
all_students = {"Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"}
math_students = {"Alice", "Bob", "Charlie", "Diana"}
science_students = {"Bob", "Diana", "Eve", "Frank"}

# Students in both courses
both_courses = math_students & science_students
print("Students in both courses:", both_courses)   # Students in both courses: {'Bob', 'Diana'}

# Students in only one course
only_math = math_students - science_students
only_science = science_students - math_students
print("Only math:", only_math)                     # Only math: {'Alice', 'Charlie'}
print("Only science:", only_science)               # Only science: {'Frank', 'Eve'}

# Students not enrolled in any course
not_enrolled = all_students - (math_students | science_students)
print("Not enrolled:", not_enrolled)               # Not enrolled: set()

# Example 27: Inventory management
available_items = {"apple", "banana", "cherry", "date", "elderberry"}
requested_items = {"banana", "cherry", "grape", "kiwi"}

# Available requested items
available = available_items & requested_items
print("Available requested items:", available)     # Available requested items: {'banana', 'cherry'}

# Unavailable requested items
unavailable = requested_items - available_items
print("Unavailable items:", unavailable)           # Unavailable items: {'grape', 'kiwi'}

# Example 28: Social network friends
alice_friends = {"Bob", "Charlie", "Diana", "Eve"}
bob_friends = {"Alice", "Charlie", "Frank", "Grace"}
charlie_friends = {"Alice", "Bob", "Diana", "Eve", "Frank"}

# Mutual friends between Alice and Bob
mutual_ab = alice_friends & bob_friends
print("Mutual friends Alice-Bob:", mutual_ab)      # Mutual friends Alice-Bob: {'Charlie'}

# Friends of friends (suggested friends for Alice)
suggested_for_alice = (bob_friends | charlie_friends) - alice_friends - {"Alice"}
print("Suggested friends for Alice:", suggested_for_alice) # Suggested friends for Alice: {'Frank', 'Grace'}

# Example 29: Tagging system
articles = [
    {"id": 1, "tags": {"python", "programming", "tutorial"}},
    {"id": 2, "tags": {"python", "data-science", "machine-learning"}},
    {"id": 3, "tags": {"javascript", "web-development", "tutorial"}},
    {"id": 4, "tags": {"python", "web-development", "django"}}
]

# Find articles with python tag
python_articles = [article["id"] for article in articles if "python" in article["tags"]]
print("Python articles:", python_articles)         # Python articles: [1, 2, 4]

# Find common tags between article 1 and 2
tags1 = next(article["tags"] for article in articles if article["id"] == 1)
tags2 = next(article["tags"] for article in articles if article["id"] == 2)
common_tags = tags1 & tags2
print("Common tags article 1 & 2:", common_tags)   # Common tags article 1 & 2: {'python'}

# Example 30: Set for data validation
valid_colors = {"red", "green", "blue", "yellow", "purple", "orange", "black", "white"}

def validate_color(color):
    if color.lower() in valid_colors:
        return f"Valid color: {color}"
    else:
        return f"Invalid color: {color}"

print(validate_color("Red"))                       # Valid color: Red
print(validate_color("Pink"))                      # Invalid color: Pink