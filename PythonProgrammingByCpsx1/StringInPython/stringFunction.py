
# String functions
# Common functions len ,  max , min , sorted
# s = 'hello world'
# print(len(s)) # 11
# print(max(s)) # w
# print(min(s)) # 
# print(sorted(s) , reversed=True ) #

# Capitalize , Title , Upper , Lower , Swapcase
# s = 'hello world'
# print(s.capitalize()) # Hello world
# print(s.title()) # Hello World      
# print(s.upper()) # HELLO WORLD
# print(s.lower()) # hello world
# s = 'HeLlO WoRlD'
# print(s.swapcase()) #llo world'
# print(s.swapcase()) #HeLlO WoRlD

# Count , Find , Index , Rfind , Rindex
# s = 'hello world'
# print(s.count('l')) # 3
# print(s.find('l')) # 2
# print(s.index('l')) # 2
# print(s.rfind('l')) # 9
# print(s.rindex('l')) # 9
# print(s.find('z')) # -1
# print(s.index('z')) # ValueError: substring not found

# endswith , startswith
# s = 'hello world'
# print(s.endswith('world')) # True
# print(s.startswith('hello')) # True

# format 
# name = 'Nitish '
# gender = 'male'
# print('My name is {} and I am a {} '.format(name , gender))
# print('My name is {1} and I am a {0} '.format(name , gender))
# print(f'My name is {name} and I am a {gender}')
# print('My name is %s and I am a %s'%(name , gender))


# isalnum , isalpha , isdigit , isidentifier
# s = 'hello123'
# print(s.isalnum()) # True
# print(s.isalpha()) # False
# print(s.isdigit()) # False
# print(s.isidentifier()) # True

# s = 'hello_123'
# print(s.isalnum()) # True

# # split , join
# s = 'hello world'
# print(s.split()) # ['hello', 'world']'
# print(s.split('o')) # ['hell', ' w', 'rld']

# l = ['hello', 'world']
# print(' '.join(l)) # hello world
# print('_'.join(l)) # hello_world

# replace , strip
s = 'hello world'
print(s.replace('hello' , 'hi')) # hi world
print(s.replace('hello' , 'hi' , 1)) # hi world

s = '  hello world  '
print(s.strip()) # hello world
print(s.lstrip()) # hello world
print(s.rstrip()) # hello world

