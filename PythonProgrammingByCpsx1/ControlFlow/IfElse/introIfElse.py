# Introduction to If-Else in Python
# If-Else statements are used for conditional execution of code blocks.
# The 'if' statement evaluates a condition, and if it is true, the associated block
# of code is executed. If the condition is false, the 'else' block (if provided) is executed.   
# Here is a simple example of If-Else statements with output in Python:

# Syntax of If-Else
# if condition:
#     # code block to be executed if condition is true
# else:
#     # code block to be executed if condition is false
# Example of If-Else in Python 
# password -> 1234

'''
email = input("Enter your email : ")
password = input("Enter your password : ")

if email == "nitish.campusx@gmail.com" and password == "1234":
    print("Welcome, you have successfully logged in!")
elif email == "nitish.campusx@gmail.com" and password != "1234":
    print("Incorrect password. Please try again.")
    password = input("Enter your password : ")
    if password == "1234":
        print("Welcome, you have successfully logged in!")
    else:
        print("Incorrect password again. Access denied.")
else:
    print("Invalid email or password. Please try again.")

    '''
# Output Example:
# Enter your email : nitish.campusx@gmail.com
# Enter your password : 1234
# Welcome, you have successfully logged in!
# Enter your email : wrongemail@gmail.com
# Enter your password : wrongpassword
# Invalid email or password. Please try again.

# WAP min of 3 numbers using if else
'''
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

if num1 <= num2 and num1 <= num3:
    print("Minimum number is : " , num1)
elif num2 <= num1 and num2 <= num3:
    print("Minimum number is : " , num2)
else:
    print("Minimum number is : " , num3)

'''

# Menu driven program using if else

'''
fnum = int(input("Enter first number : "))
snum = int(input("Enter second number : "))

op = input("Enter operation (+, -, *, /) : ")
if op == "+":
    print("Addition is : " , fnum + snum)
elif op == "-":
    print("Subtraction is : " , fnum - snum)
elif op == "*":
    print("Multiplication is : " , fnum * snum)
elif op == "/":
    print("Division is : " , fnum / snum)
else:
    print("Invalid operation")         


'''
# Output Example:
# Enter first number : 10
# Enter second number : 5
# Enter operation (+, -, *, /) : +
# Addition is :  15
# Enter first number : 10
# Enter second number : 5
# Enter operation (+, -, *, /) : /
# Division is :  2.0
# Enter first number : 10
# Enter second number : 5

# Menu driven program for balance enquiry using if else

menu = input(""" 
Hi , How can I help you today?
1. Enter 1 for pin change
2. Enter 2 for balance enquiry
3. Enter 3 for cash withdrawal
4. Enter 4 for exit
Please enter your choice: """)

if menu == "1":
    print("You have selected pin change.")
    # Add pin change logic here
elif menu == "2":
    print("Your balance is $1000.")
    # Add balance enquiry logic here
elif menu == "3":
    print("You have selected cash withdrawal.")
    # Add cash withdrawal logic here
elif menu == "4":
    print("Thank you for using our services. Goodbye!")
else:
    print("Invalid choice. Please try again.")
# Output Example:
# Hi , How can I help you today?
# 1. Enter 1 for pin change
# 2. Enter 2 for balance enquiry
# 3. Enter 3 for cash withdrawal    
# 4. Enter 4 for exit
# Please enter your choice: 2   
# Your balance is $1000.
# Hi , How can I help you today?
# 1. Enter 1 for pin change