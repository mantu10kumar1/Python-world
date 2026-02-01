### `Problem 1`: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:

# > Salary(Lakhs) : Tax(%)

# *   Below 5 : 0%
# *   5-10 : 10%
# *   10-20 : 20%
# *   aboove 20 : 30%

# ctc = int(input("Enter CTC : "))
# salary = ctc * 100000
# hra = salary * 0.1
# da = salary * 0.05
# pf = salary * 0.03
# if salary < 500000:
#     tax = 0
# elif salary >= 500000 and salary < 1000000:
#     tax = salary * 0.10
# elif salary >= 1000000 and salary < 2000000:
#     tax = salary * 0.20
# else:
#     tax = salary * 0.30
# in_hand_salary = salary - hra - da - pf - tax
# print("In hand salary is : " , in_hand_salary)


### `Problem 2`: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
# first = int(input("Enter first angle : "))
# second = int(input("Enter second angle : "))
# third = int(input("Enter third angle : "))

# if first + second + third == 180 and first > 0 and second > 0 and third > 0:
#     print("It can form a triangle")
# else:
#     print("It can't form a triangle")

### `Problem 3`: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.
# cost_price = int(input("Enter cost price : "))
# selling_price = int(input("Enter selling price : "))

# if selling_price > cost_price:
#     print("Profit")
# elif selling_price < cost_price:
#     print("Loss")
# else:
#     print("No Loss No Profit")

### `Problem 4`: Write a menu-driven program -
# 1. cm to ft
# 2. km to miles
# 3. USD to INR
# 4. exit

# menu = input("""
# 1. cm to ft
# 2. km to miles
# 3. USD to INR
# 4. exit : """)

# if menu == '1':
#     cm = float(input("Enter cm : "))
#     ft = cm * 0.0328
#     print("ft : " , ft)
# elif menu == '2':
#     km = float(input("Enter km : "))
#     miles = km * 0.621
#     print("miles : " , miles)
# elif menu == '3':
#     usd = float(input("Enter usd : "))
#     inr = usd * 82.41
#     print("inr : " , inr)
# else:
#     print("Exit")


### `Problem 5` - Exercise 12: Display Fibonacci series up to 10 terms.
# *Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34*
# num1 , num2 = 0 , 1
# for i in range(10):
#     print(num1)
#     next = num1 + num2
#     num1 = num2
#     num2 = next

### `Problem 6` - Find the factorial of a given number.
# Write a program to use the loop to find the factorial of a given number.
# The factorial (symbol: `!`) means to multiply all whole numbers from the chosen number down to 1.
# For example: calculate the factorial of 5
# ```bash
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# ```
# Output:
# ```bash
# 120

# num = int(input("Enter a number : "))
# fact = 1
# for i in range(1 , num + 1):
#     fact = fact * i
# print("Factorial is : " , fact)

### `Problem 7` - Reverse a given integer number.
# Example:
# `Input:`
# ```bash
# 76542
# ```
# `Output:`
# ```bash
# 24567
# ```

# num = int(input("Enter a number : "))
# rev = 0
# while num > 0:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10
# print("Reverse is : " , rev)

### `Problem 8`: Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible by 5, then skip that number. And if the sum is greater than 300, don't need to calculate the sum further more. Print the final result. And don't use for loop to solve this problem.
# **Example 1:**
# `Input:`
# ```bash
# 30
# ```
# `Output:`
# ```bash
# 276
# ```

# N = int(input("Enter a number : "))
# sum = 0
# for i in range(1 , N + 1):
#     if i % 5 == 0:
#         continue
#     sum = sum + i
#     if sum > 300:
#         break
# print("Sum is : " , sum)

### `Problem 9`: Write a program that keeps on accepting a number from the user until the user enters Zero. Display
#  the sum and average of all the numbers.
# sum = 0
# count = 0
# while True:
#     num = int(input("Enter a number : "))
#     if num == 0:
#         break
#     sum = sum + num
#     count = count + 1
# print("Sum is : " , sum)
# print("Average is : " , sum / count)

###`Problem 9`: Write a program which will find all such numbers which are divisible by 7
#  but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed 
# in a comma-separated sequence on a single line.
# L = []
# for i in range(2000 , 3201):
#     if i % 7 == 0 and i % 5 != 0:
#         L.append(str(i))
# print(',' . join(L))

###`Problem 10`: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a space-separated sequence on a single line.

# L = []
# for i in range(1000 , 3001):
#     s = str(i)
#     if int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 0 and int(s[3]) % 2 == 0:
#         L.append(s)
# print(' '.join(L))


###`Problem 11`: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# ```
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# !
# ```
# > The numbers after the direction are steps.
# > `!` means robot stop there.
# **Please write a program to compute the distance from current position after a sequence of movement and original point.**
# *If the distance is a float, then just print the nearest integer.*
# Example:
# `Input`:
# ```
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# !
# ```
# `Output`:
# ```
# 2
# ```
# pos = [0 , 0]
# while True:
#     s = input("Enter the robot path : ")
#     if s == '!':
#         break
#     direction = s.split()[0]
#     steps = int(s.split()[1])
#     if direction == 'UP':
#         pos[0] = pos[0] + steps
#     elif direction == 'DOWN':
#         pos[0] = pos[0] - steps
#     elif direction == 'LEFT':
#         pos[1] = pos[1] - steps
#     elif direction == 'RIGHT':
#         pos[1] = pos[1] + steps
#     else:
#         pass
# print(pos)
# distance = ((pos[0]**2) + (pos[1]**2))**0.5
# print(round(distance))


###`Problem 12`:Write a program to print whether a given number is a prime number or not
num = int(input("Enter a number : "))
if num > 1: 
    for i in range(2 , num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")
