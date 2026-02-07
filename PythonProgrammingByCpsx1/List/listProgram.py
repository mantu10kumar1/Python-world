# List Definition : 
# A list in Python is a mutable, ordered collection of items (elements) that can be of different data types.
# Lists are one of Python's most versatile and commonly used data structures .
# Key Characteristics
# Mutable
# Ordered
# Dynamic
# Heterogeneous
# Indexable and slicable
# Iterable

# Creation of List with example and with homogenious typs of data
# Empty
# L = []
# print("This is the Empty list : " , L)

# # 1D List creation
# l = [1,2,3,4,5] 
# print("This is the 1D list : " , l)

# # 2D List
# l = [[1,2,3],[4,5,6]]
# print("This is the 2D list : " , l)

# # 3D List
# l = [[[1,2],[3,4]],[[5,6],[7,8]]]
# print("This is the 3D list : " , l)


# Creation of List with example and with Hetrogenious type of data
# l = [1, "Hello" , ' World ' , 5.6 , 3+4j ,True , ]
# print("This is the Hetrogenious list : " , l)


# Accessing items from the list with positive index with output
# l  = [1,2,3,4,5]
# print(l[0])        # 1
# print(l[1])        # 2
# print(l[2])        # 3


# l2 = [[1,2,3],[4,5,6],[7,8,9]]
# print(l2[0][0])     # 1
# print(l2[1][1])     # 5
# print(l2[2][2])     # 9


# Accessing items from the list with negative index
# l  = [1,2,3,4,5]
# print(l[-1])        # 5
# print(l[-2])        # 4
# print(l[-3])        # 3

# l2 = [[1,2,3],[4,5,6],[7,8,9]]
# print(l2[-1][-1])     # 9
# print(l2[-2][-2])     # 5
# print(l2[-3][-3])     # 1


# Slicing
# l = [1,2,3,4,5,6,7,8,9,10]
# print(l[-3:])            #  [8, 9, 10]
# print(l[2:-3])           #  [3, 4, 5, 6, 7]
# print(l[1:])             #  [2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(l[:])              #  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(l[::2])            #  [1, 3, 5, 7, 9]
# print(l[::-1])
# print(l[1:10:2])         #  [2, 4, 6, 8, 10]


# Functions with list with examples and output
# append
# l = [1,2,3,4,5]
# l.append(6)
# print(l)                   # [1, 2, 3, 4, 5, 6]
# l = [1,2,3,4,5]
# l.append([6,7,8]) 
# print(l)                     # [1, 2, 3, 4, 5, [6, 7, 8]]

# # insert
# l.insert(2,7)
# print(l)                   # [1, 2, 7, 3, 4, 5, 6]

# # pop
# l.pop()
# print(l)                   # [1, 2, 7, 3, 4, 5]

# push
# l = [1,2,3,4,5]
# l.append(6)
# print(l)                   # [1, 2, 3, 4, 5, 6]
# l.push(7)                  #  AttributeError: 'list' object has no attribute 'push'
# print(l)                   # [1, 2, 3, 4, 5, 6, 7]





# # remove
# l.remove(2)
# print(l)                   # [1, 7, 3, 4, 5]

# # reverse
# l.reverse()
# print(l)                   # [5, 4, 3, 7, 1]

# # sort
# l.sort()
# print(l)                   # [1, 3, 4, 5, 7]

# # extend
# l.extend([8,9,10])
# print(l)                   # [1, 3, 4, 5, 7, 8, 9, 10]
# l = [1,2,3,4,5]
# l2 = [6,7,8,9,10]
# l.extend(l2)
# print(l)                     # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# l = [1,2,3,4,5]
# l.extend("Hello")
# print(l)                      # [1, 2, 3, 4, 5, 'H', 'e', 'l', 'l', 'o']

# # count
# print(l.count(3))          # 1

# # index
# print(l.index(5))          # 4

# # clear
# l.clear()
# print(l)                   # []

# # copy
# l = [1,2,3,4,5]
# l2 = l.copy()
# print(l2)                  # [1, 2, 3, 4, 5]

# # len
# print(len(l))              # 5

# # min
# print(min(l))              # 1

# # max
# print(max(l))              # 5

# # sum
# print(sum(l))              # 15

# # sorted
# print(sorted(l))           # [1, 2, 3, 4, 5]

# # any
# print(any(l))              # True

# # all
# print(all(l))              # True

# # enumerate
# for i,j in enumerate(l):
#     print(i,j)
#     # 0 1
#     # 1 2
#     # 2 3
#     # 3 4
#     # 4 5


# Editing with indexing
# l = [1,2,3,4,5]
# l[0] = 6
# print(l)                # [6, 2, 3, 4, 5]


# # Editing with slice 
# l[1:4] = [70,80,90]
# print(l)                # [6, 70, 80, 90, 5]

# del with list 
# l = [1,2,3,4,5]
# del l[0]
# print(l)                # [2, 3, 4, 5]

# del l[1:3]
# print(l)                # [2, 5]

# Operation on Lists
   # Arithmetic
   # Membership
   # Loop 

 # Arithmetic
# l = [1,2,3,4,5]
# l2 = [6,7,8,9,10]
# print(l+l2)             # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(l*3)              # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# Membership
# l = [1,2,3,4,5]
# print(2 in l)           # True
# print(6 in l)           # False
# print(2 not in l)       # False
# print(6 not in l)       # True
# l = [[1,2,3],[4,5,6],[7,8,9]]
# print([1,2,3] in l)     # True
# print([1,2] in [1,2,3,4,5])     # False     # 
# print([2,3] in l)                # False

# Loop
# for i in l:
#     print(i)
# # 1
# # 2
# # 3
# # 4
# # 5


# Sort vs sorted
# l = [1,2,3,4,5]
# l.sort()
# print(l)                # [1, 2, 3, 4, 5]
# l2 = [6,7,8,9,10]
# print(sorted(l2))       # [6, 7, 8, 9, 10]  

# sorted is a temprory operation there is no change in original value
# sort is change the original value

# Copy  --> it shallow copy
l = [1,2,3,4,5]
print(l)
print(id(l))
l2 = l.copy()
print(l2)               # [1, 2, 3, 4,5]
print(id(l2))