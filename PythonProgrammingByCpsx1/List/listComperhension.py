# Syntax 
#  newlist = [expression for item in iterable if condition == True]


# Without list comperhension
# l = []
# for i in range(1,11):
#     l.append(i)
# print(l)

# # With list comperhension
# l = [i for i in range(1,11)]
# print(l)

# Multiplication on vector
# without comperhension
# l = []
# for i in range(1,11):
#     l.append(i*2)
# print(l)

# # With comperhension
# l = [i*2 for i in range(1,11)]
# print(l)

# store a square in list
# without comperhension
# l = []
# for i in range(1,11):
#     l.append(i**2)
# print(l)

# # With comperhension
# l = [i**2 for i in range(1,11)]
# print(l)

# print all the no divisible by 5 in ther range of 1 to 100
# l = [i for i in range(1,101) if i%5==0]
# print(l)

# print all the words start with p
# languages = ["java" , "python" , "php" , "c" , "c++"]
# newLang = [language for language in languages if language.startswith("p")]
# print(newLang)

# Nested if 
# basket = ['apple', 'guava' , 'cherry','banana']
# my_fruits = ['apple' , 'kiwi' , 'grapes' , 'banana']
# result = [fruit for fruit in my_fruits if fruit in basket if fruit.startswith('a')]
# print(result)

# list with matrix
# matrix = [[i for i in range(5)] for j in range(3)]
# print(matrix)

# calculate the cartesian product
# l1 = [1 , 2 , 3 , 4]
# l2 = [5 , 6 , 7 , 8]
# result = [i*j for i in l1 for j in l2]
# print(result)


# Two way to traveral of list
# Item wise
# l = [11,12,13,14,15]
# for i in l:
#     print(i,end=" ")

# print()

# # Index wise
# for i in range(len(l)):
#     print(l[i] , end=" ")

# Zip function
# l1 = [1,2,3,4]
# l2 = [-1,-2,-3,-4]
# print(list(zip(l1,l2)))
# # [(1, -1), (2, -2), (3, -3), (4, -4)]
# add = [i+j for i,j in zip(l1,l2)]
# print(add)          

# l = [1 , 2 , print , type , input]
# print(l)


a = [1,2,3]
b = a.copy()

print(a)
print(b)

a.append(4)
print(a)
print(b)