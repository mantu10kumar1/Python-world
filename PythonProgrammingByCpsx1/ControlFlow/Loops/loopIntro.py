# Loop in Python
# Definition : It is used perform repeated tasks
# There is two types of loops 
# 1. While loop : When we don't  know the number iteration then we use while loop

# Print table of any number

'''
num = int(input("Enter the number : "))
i = 1
while i<11:
    print(i , " * " , num , " = " , i * num)
    i = i + 1

else: 
    print("Limit cross")

'''


'''
# Create a guessing number game
import random
jackpot = random.randint(1 , 10)

guess = int(input("guess karo : "))
counter = 1 
while guess != jackpot:
    if guess < jackpot:
        print("Galat guess higer ")
    else:
        print("Galat ! guess lower ")
    
    guess = int(input("guess karo : "))
    counter +=1

else:
    print("Correct guess ")
    print("attempts : " , counter)

'''

# for loop : when know the number of iteration then we use for loop
'''
for i in range(1 , 11):
    print(i)

for i in range(1 , 11 , 2):
    print(i)

for i in "Delhi":
    print(i)

'''
# Program - The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. 
# you have to write a program to find out the population at the end of each of the last 10 years
curr_pop = 10000
for i in range(10 , 0 , -1):
    print(i , curr_pop)
    curr_pop = curr_pop - 0.1*curr_pop