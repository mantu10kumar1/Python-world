# What is string : 

# # Creation of string 
# s = 'hello world'
# s = "hello world"
# # Multiline
# s = '''hello world'''
# s = """hello world"""
# s = str('hello world')
# print(s)


# # Indexing
# # Positige indexing
# s = 'hello world'
# print(s[0]) # h
# print(s[1]) # e
# print(s[2]) # l

# # Negative indexing
# print(s[-1]) # d
# print(s[-2]) # l
# print(s[-3]) # r

# Slicing
# s = 'hello world'
# print(s[0:5]) # hello
# print(s[6:11]) # world
# print(s[:5]) # hello
# print(s[6:]) # world
# print(s[:]) # hello world
# # with stpes
# print(s[0:5:2]) # hlo
# print(s[6:11:2]) # wrd

# print(s[6:0:-1]) # w olle
# print(s[::-1])

# print(s[-5:]) # world
# print(s[-1:-6:-1])  # dlrow


# Editing and Deleting in String
# s = 'hello world'
# s[0] = 'H' # TypeError: 'str' object does not support item assignment
# del s[0] # TypeError: 'str' object doesn't support item deletion
# del s
# print(s) # NameError: name 's' is not defined

# String with Operators list
# Arithmetic Operations
# Concatenation
# Loops on String
# Membership Operator

# print('Delhi ' + ' Mumbai') # Delhi Mumbai
# print('Delhi ' * 3) # Delhi Delhi Delhi

# print('Delhi' in 'Delhi Mumbai') # True
# print('Delhi' not in 'Delhi Mumbai') # False

# for i in 'Delhi':
#     print(i)

# print('Pune' > 'pune') # False
# print('Pune' < 'pune') # True
# print('Pune' == 'pune') # False
# print('Pune' != 'pune') # True
# print('Pune' >= 'pune') # True
# print('Pune' <= 'pune') # False

# print('hello' and 'world') # world
# print('hello' or 'world') # hello
# print(not 'hello') # False
# print(not '') # True
# print('' and 'world') # ''
# print('' or 'world') # world

# for i in 'hello':
#     print('World..')
