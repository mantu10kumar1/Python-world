# Definition : A tuple in python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once 
# it is assigned whereas we can change the elements of a list.

# Characterstics :
#1. Ordered
#2. Unchangeable
#3. Allow duplicate

# Plan of attack
#1. Creating a Tuple
#2. Accessing items
#3. Editing items
#4. Adding items
#5. Deleting items
#6. Operation on tuple
#7. Tuple Functions

# # 1. Creating a tuple
# t1 = ()
# print(t1)            # ()
# print(type(t1))      # <class 'tuple'>

# t = (2)
# print(t)             # 2
# print(type(t))       # <class 'int'>

# t2 = (2,)
# print(t2)            # (2,)
# print(type(t2))      # <class 'tuple'>

# # Homogenious
# t3 = (1,2,3,4,5)
# print(t3)            # (1, 2, 3, 4, 5)
# print(type(t3))      # <class 'tuple'>

# # Heterogenious
# t = (1 , 2 , True , [1,2,3])
# print(t)            # (1, 2, True, [1, 2, 3])
# print(type(t))      # <class 'tuple'>

# # Nested tuples
# t4 = (1,2 ,3, (4,5,6))
# print(t4)           # (1, 2, 3, (4, 5, 6))
# print(type(t4))     # <class 'tuple'>

# #  Using type conversion
# t5 = tuple('hello')
# print(t5)           # ('h', 'e', 'l', 'l', 'o')
# print(type(t5))     # <class 'tuple'>


fruits = ("apple", "banana", "cherry", "banana", "date")
print("Index of 'banana':", fruits.index("banana"))
print("Index of 'banana' from position 2:", fruits.index("banana", 2))