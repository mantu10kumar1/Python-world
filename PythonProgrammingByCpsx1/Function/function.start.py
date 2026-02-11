def is_even(num):
    """
    Docstring for is_even
    :param num: Input number
    This function checks and prints if a given number is even or odd.
    """
    if type(num) == int:
        if num % 2 == 0:
            # f-string use kiya gaya hai
            print(f"The number {num} is even")
        else:
            print(f"The number {num} is odd")
    else:
        print("Pagal hai kya")

# Loop to test
for i in range(1, 11):
    is_even(i)

# Docstring print
print(is_even.__doc__)

# Extra tests
is_even(5)
is_even("hello")


# -*- coding: utf-8 -*-
"""session6-functions.ipynb"""

### Let's create a function(with docstring)

def is_even(num):
  """
  This function returns if a given number is odd or even
  input - any valid integer
  output - odd/even
  created on - 16th Nov 2022
  """
  if type(num) == int:
    if num % 2 == 0:
      return 'even'
    else:
      return 'odd'
  else:
    return 'pagal hai kya?'

# function_name(input)
for i in range(1,11):
  x = is_even(i)
  print(x)
  # Output Line by Line:
  # odd
  # even
  # odd
  # even
  # odd
  # even
  # odd
  # even
  # odd
  # even

print(type.__doc__) 
# Output: type(object) -> the object's type... (Poora type function ka documentation print hoga)

### 2 Point of views
print(is_even('hello')) # pagal hai kya?

### Types of Arguments
def power(a=1,b=1):
  return a**b

print(power())         # 1
print(power(2,3))      # 8 (positional)
print(power(b=3,a=2))  # 8 (keyword)

### *args and **kwargs
def multiply(*kwargs):
  product = 1 
  for i in kwargs:
    product = product * i

  print(kwargs)        # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12)
  return product

print(multiply(1,2,3,4,5,6,7,8,9,10,12)) # 43545600

# **kwargs
def display(**salman):
  for (key,value) in salman.items():
    print(key,'->',value)
    # Output:
    # india -> delhi
    # srilanka -> colombo
    # nepal -> kathmandu
    # pakistan -> islamabad

display(india='delhi',srilanka='colombo',nepal='kathmandu',pakistan='islamabad')

### Without return statement
L = [1,2,3]
print(L.append(4))     # None (Kyunki append() kuch return nahi karta)
print(L)                # [1, 2, 3, 4]

### Variable Scope
def g(y):
    print(x)           # 5
    print(x+1)         # 6
x = 5
g(x)
print(x)               # 5

def f(y):
    x = 1
    x += 1
    print(x)           # 2
x = 5
f(x)
print(x)               # 5

def h(y):
    # Yeh error dega agar 'global x' na likha ho, 
    # par scope context ke hisab se agar x define hai:
    pass 
x = 5
h(x)
print(x)               # 5

def f(x):
   x = x + 1
   print('in f(x): x =', x) # in f(x): x = 4
   return x

x = 3
z = f(x)
print('in main program scope: z =', z) # in main program scope: z = 4
print('in main program scope: x =', x) # in main program scope: x = 3

### Nested Functions
# f() call karne par recursion depth error aayega kyunki f, g ko aur g, f ko call kar raha hai.

def g(x):
    def h(x):
        x = x+1
        print("in h(x): x = ", x) # in h(x): x = 5
    x = x + 1
    print('in g(x): x = ', x)    # in g(x): x = 4
    h(x)
    return x

x = 3
z = g(x)
print('in main program scope: x = ', x) # in main program scope: x = 3
print('in main program scope: z = ', z) # in main program scope: z = 4

### Functions are 1st class citizens
def square(num):
  return num**2

print(type(square))    # <class 'function'>
print(id(square))      # (Memory address like 1407...)

# reassign
x = square
print(x(3))            # 9

# returning a function
def f():
    def x(a, b):
        return a+b
    return x

val = f()(3,4)
print(val)             # 7

# function as argument
def func_a():
    print('inside func_a') # inside func_a (jab func_b call hoga)

def func_b(z):
    print('inside func_c') # inside func_c
    return z()

print(func_b(func_a))  
# Output sequence: 
# inside func_c
# inside func_a
# None (Kyunki func_a kuch return nahi kar raha)

### Lambda Function
a = lambda x,y:x+y
print(a(5,2))          # 7

a = lambda s:'a' in s
print(a('hello'))      # False

a = lambda x:'even' if x%2 == 0 else 'odd'
print(a(6))            # even

### Higher Order Functions
def transform(f,L):
  output = []
  for i in L:
    output.append(f(i))
  print(output)        # [1, 8, 27, 64, 125]

L = [1,2,3,4,5]
transform(lambda x:x**3,L)

### Map
print(list(map(lambda x:x**2,[1,2,3,4,5]))) # [1, 4, 9, 16, 25]

### Filter
L = [3,4,5,6,7]
print(list(filter(lambda x:x>5,L)))         # [6, 7]

### Reduce
import functools
print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5])) # 15
print(functools.reduce(lambda x,y:x if x>y else y,[23,11,45,10,1])) # 45