### --- PYTHON LISTS TASK SOLUTIONS --- ###

### Problem 1: Combine two lists index-wise (columns wise)
# list1 = ["M", "na", "i", "Kh"]
# list2 = ["y", "me", "s", "an"]

# # zip() function ka use karke pairs banaye aur list() mein convert kiya
# result1 = [list(i) for i in zip(list1, list2)]
# result2 = [[i , j] for i , j in zip(list1 , list2)]

# # Agar lists ki length alag hoti toh itertools.zip_longest use karte
# print("Problem 1 Output:", result1)              # [['M', 'y'], ['na', 'me'], ['i', 's'], ['Kh', 'an']]
# print("Problem 1 Output:", result2)              # [['M', 'y'], ['na', 'me'], ['i', 's'], ['Kh', 'an']]




### Problem 2: Add new item to list after a specified item (7000 after 6000)
# list1_p2 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# # Nested indexing ka use karke append kiya
# list1_p2[2][2].append(7000)
# print("Problem 2 Output:", list1_p2)              # [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]


### Problem 3: Update no of items available
# candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
# no_of_items = [10,20,34,74,32]

# print("Problem 3 Output:")
# for candy, count in zip(candy_list, no_of_items):
#     print(f"{candy}-{count}")                    # Jelly Belly-10, etc.


### Problem 4: Running Sum on list
# list1_p4 = [1,2,3,4,5,6]
# running_sum = []
# current_total = 0

# for num in list1_p4:
#     current_total += num
#     running_sum.append(current_total)

# print("Problem 4 Output:", running_sum)           # [1, 3, 6, 10, 15, 21]


### Problem 5: Elements greater than and itself
# list1_p5 = [2, 4, 6, 10, 1]
# result5 = []

# for i in list1_p5:
#     sum_val = i
#     for j in list1_p5:
#         if j > i:
#             sum_val += j
#     result5.append(sum_val)

# print("Problem 5 Output:", result5)              # [22, 20, 16, 10, 23]


### Problem 6: Common unique items in increasing order
# num1 = [23,45,67,78,89,34]
# num2 = [34,89,55,56,39,67]
# common2 = []

# # Sets ka use karke intersection nikala aur sort kiya
# common = sorted(list(set(num1) & set(num2)))
# print("Problem 6 Output:", common)               # [34, 67, 89]

# for i in num1:
#     if i in num2:
#         if i not in common2:
#             common2.append(i)

# print("Problem 6 Output:", common2)              # [34, 67, 89]




### Problem 7: Sort alphanumeric strings based on product of numeric characters
def get_product(s):
    prod = 1
    has_digit = False
    for char in s:
        if char.isdigit():
            prod *= int(char)
            has_digit = True
    return prod if has_digit else 1

input_list7 = ['1ac21', '23fg', '456', '098d','1','kls']
# Product function ke basis par sort kiya
result7 = sorted(input_list7, key=get_product)
print("Problem 7 Output:", result7)              # ['456', '23fg', '1ac21', '1', 'kls', '098d'] (0*9*8=0 is smallest)


### Problem 8: Split String of list on K character (Space)
# input_list8 = ['CampusX is a channel', 'for data-science', 'aspirants.']
# result8 = []
# for sentence in input_list8:
#     result8.extend(sentence.split())

# print("Problem 8 Output:", result8)              # ['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']


### Problem 9: Convert Character Matrix to single String
# matrix9 = [['c', 'a', 'm', 'p', 'u', 'x'], ['i', 's'], ['b', 'e', 's', 't'], ['c', 'h', 'a', 'n', 'n', 'e', 'l']]
# List comprehension aur join ka use
# result9 = " ".join(["".join(word) for word in matrix9])
# print("Problem 9 Output:", result9)              # campux is best channel


### Problem 10: Add Space between Potential Words (CamelCase to Space)
# input_list10 = ['campusxIs', 'bestFor', 'dataScientist']
# result10 = []

# for s in input_list10:
#     temp = ""
#     for char in s:
#         if char.isupper():
#             temp += " " + char
#         else:
#             temp += char
#     result10.append(temp)

# print("Problem 10 Output:", result10)            # ['campusx Is', 'best For', 'data Scientist']


### Problem 11: Union operation on 2 lists
# l1 = [1,2,3,4,5,1]
# l2 = [2,3,5,7,8]
# # Set union duplicates ko automatically handle karta hai
# union_res = list(set(l1) | set(l2))
# print("Problem 11 Output:", union_res)           # [1, 2, 3, 4, 5, 7, 8]


### Problem 12: Max number of each row of a matrix
# matrix12 = [[1,2,3],[4,5,6],[7,8,9]]
# result12 = [max(row) for row in matrix12]
# print("Problem 12 Output:", result12)            # [3, 6, 9]


### Problem 13: List comprehension for specific matrix
# 0 se 8 tak numbers ko 3-3 ke chunks mein divide kiya
# result13 = [[i, i+1, i+2] for i in range(0, 9, 3)]
# print("Problem 13 Output:", result13)            # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


### Problem 14: Transpose a given matrix
# matrix14 = [[1,2,3], [4,5,6], [7,8,9]]
# # Rows ko columns aur columns ko rows banaya
# transpose = [[row[i] for row in matrix14] for i in range(len(matrix14[0]))]
# print("Problem 14 Output:", transpose)           # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


### Problem 15: Flatten a nested list
# matrix15 = [[1,2,3], [4,5,6], [7,8,9]]
# # Nested loop in list comprehension
# flatten = [num for row in matrix15 for num in row]
# print("Problem 15 Output:", flatten)             # [1, 2, 3, 4, 5, 6, 7, 8, 9]