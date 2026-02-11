# Q1: Join Tuples if similar initial element
test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
res = []
for i in test_list:
    if res and res[-1][0] == i[0]:
        res[-1] = res[-1] + i[1:]
    else:
        res.append(i)
print("Q1 Output:", res)                         # [(5, 6, 7, 8), (6, 10), (7, 13)]

# Q2: Multiply Adjacent elements (both side) and take sum
t = (1, 5, 7, 8, 10)
res = []
for i in range(len(t)):
    if i == 0:
        res.append(t[i] * t[i+1])
    elif i == len(t) - 1:
        res.append(t[i] * t[i-1])
    else:
        res.append(t[i]*t[i-1] + t[i]*t[i+1])
print("Q2 Output:", tuple(res))                  # (5, 40, 91, 136, 80)

# Q3: Check is tuples are same or not
t1 = (1, 2, 3, 0)
t2 = (0, 1, 2, 3)
res = "same" if t1 == t2 else "not same"
print("Q3 Output:", res)                         # not same

# Q4: Count no of tuples, list and set from a list
list1 = [{'hi', 'bye'},{'Geeks', 'forGeeks'},('a', 'b'),['hi', 'bye'],['a', 'b']]
c_list, c_set, c_tuple = 0, 0, 0
for i in list1:
    if type(i) == list: c_list += 1
    elif type(i) == set: c_set += 1
    elif type(i) == tuple: c_tuple += 1
print(f"Q4 Output: List-{c_list}, Set-{c_set}, Tuples-{c_tuple}") # List-2, Set-2, Tuples-1

# Q5: Shortlist Students for a Job role
# Input format for testing: records=1, Manohar, B.Tech, Python, 2022. Requirement: Python, B.Tech, 2022.
records = [('Manohar', 'B.Tech', 'Python', '2022'), ('Ponian', 'B.Sc.', 'C++', '2020')]
req_skill, req_edu, req_year = 'Python', 'B.Tech', '2022'
found = False
for s in records:
    if s[2] == req_skill and s[1] == req_edu and s[3] == req_year:
        print("Q5 Output:", s)                   # ('Manohar', 'B.Tech', 'Python', '2022')
        found = True
if not found: print("No such candidate")

# Q1: Common elements in three lists using sets
ar1, ar2, ar3 = [1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100], [3, 4, 15, 20, 30, 70, 80, 120]
res = list(set(ar1) & set(ar2) & set(ar3))
print("Q1 Output:", res)                         # [80, 20]

# Q2: Count unique number of vowels
Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
vowels = "aeiouAEIOU"
unique_vowels = {char for char in Str1 if char in vowels}
print("Q2 Output: No of unique vowels-", len(unique_vowels)) # No of unique vowels-6

# Q3: Check if string is binary (only two unique characters)
s = "01010101010"
res = "Yes" if len(set(s)) == 2 else "No"
print("Q3 Output:", res)                         # Yes

# Q4: Find union of n arrays
arrays = [[1, 2, 2, 4, 3, 6], [5, 1, 3, 4], [9, 5, 7, 1], [2, 4, 1, 3]]
res = set().union(*arrays)
print("Q4 Output:", sorted(list(res)))           # [1, 2, 3, 4, 5, 6, 7, 9]

# Q5: Intersection of two lists (List Comprehension)
lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}
res = [x for x in lst1 if x in lst2]
print("Q5 Output:", res)                         # [9, 10, 4, 5]

# Q1: Key with maximum unique values
test_dict = {"CampusX" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}
res = max(test_dict, key=lambda k: len(set(test_dict[k])))
print("Q1 Output:", res)                         # CampusX

# Q2: Replace words from Dictionary
test_str = 'CampusX best for DS students.'
repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}
res = " ".join([repl_dict.get(word, word) for word in test_str.split()])
# Note: Cleaning '.' for perfect match
print("Q2 Output:", res.replace(' students.', ' students.')) # CampusX is the best channel for Data-Science students.

# Q3: Convert List to List of dictionaries
test_list, key_list = ["DataScience", 3, "is", 8], ["name", "id"]
res = [{key_list[0]: test_list[i], key_list[1]: test_list[i+1]} for i in range(0, len(test_list), 2)]
print("Q3 Output:", res)                         # [{'name': 'DataScience', 'id': 3}, {'name': 'is', 'id': 8}]

# Q4: Convert a list of Tuples into Dictionary
tup_list = [("akash", 10), ("gaurav", 12), ("anand", 14)]
res = {k: [v] for k, v in tup_list}
print("Q4 Output:", res)                         # {'akash': [10], 'gaurav': [12], 'anand': [14]}

# Q5: Sort Dictionary key and values List
d = {'c': [3], 'b': [12, 10], 'a': [19, 4]}
res = {k: sorted(v) for k, v in sorted(d.items())}
print("Q5 Output:", res)                         # {'a': [4, 19], 'b': [10, 12], 'c': [3]}