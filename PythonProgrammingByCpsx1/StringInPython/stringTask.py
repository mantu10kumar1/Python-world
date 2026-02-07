# Find the length of a given string without using the len() function

# s = input("Enter a string: ")
# counter = 0
# for i in s:
#     counter += 1
# print("Length of the string is:", counter)

# Task2 extract username fom a given email
# s = input("Enter your email: ")
# pos = s.index("@")
# print(s[0:pos])

# Task3 count the frequency of a particular character in a provided string
# s = input("Enter a string : ")
# char = input("Enter a character : ")
# counter = 0
# for i in s:
#     if i == char:
#         counter += 1
# print("Frequency of",char,"is:",counter)

# Task4 Write a program which can remove a particular character from a string
# s = input("Enter a string : ")
# char = input("Enter a character : ")
# ans = ""
# for i in s:
#     if i != char:
#         ans += i
# print("After removing",char,"is: " ,ans)

# Task5 Write a program that can check whether a given string is palindrome or not
# s = input("Enter a string : ")
# flag = True
# for i in range(0,len(s)//2):
#     if s[i] != s[len(s) - i - 1]:
#         flag = False
#         print("The give string is Not a palindrome")
#         break
# if flag:
#     print("The given string is a palindrome ")

# Task 6 write a program that count the word in the give string
# s = input("Enter a string : ")
# temp = ''
# counter = 0
# for i in s:
#     if i != ' ':
#         temp += i
#     else:
#         counter += 1
# if temp != '':
#     counter += 1

# print("No. of words in the given string is : " , counter)

# Task 7 Write a program o convert a string to title case without using title() function
# s = input("Enter a string : ")
# l = s.split()
# ans = ""
# for word in l:
#     ans = ans + word[0].upper() + word[1:].lower() + " "
# print(ans)

# Task 8 Write a program that can convert an integer to string
number = int(input("Enter a number : "))
digits = "0123456789"
result = ""
while number != 0:
    result = digits[number % 10] + result
    number = number // 10
print(result)
print(type(result))


