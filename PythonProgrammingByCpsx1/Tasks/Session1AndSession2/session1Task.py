# Task1 
# "Data" "Science" "Mentorship" "Program"
# "By" "CampusX"

# Write your code here
# celcius = float(input('Enter the temp in celcius : '))
# faren = celcius * (9/5) + 32
# print(faren , "F")

# Task2 swap 2 numbers
# a = 3
# b = 5
# a , b = b , a
# print(a)
# print(b)

# a = 3 
# b = 5
# print("Before swaping value of a : " , a)
# print("Before swaping value of b : " , b)
# temp = a 
# a = b
# b = temp
# print("After swaping value of a : " , a)
# print("After swaping value of b : " , b)

# Task3 
# Write your code here
# celcius = float(input('Enter the temp in celcius : '))
# faren = celcius * (9/5) + 32
# print(faren , "F")
# print("Hi..")

# Task 4 Calculate Ecludean distance
# p1x = int(input('Enter x cood of 1st point : '))
# p1y = int(input('Enter y cood of 1st point : '))
# p2x = int(input('Enter x cood of 2nd point : '))
# p2y = int(input('Enter y cood of 2nd point : '))

# distance = ((p2x - p1x)**2 + (p2y - p1y)**2)**0.5
# print("The Euclidean distance between two coordinates is : " , round(distance , 3))

# Task 5 Calculate interest
# p = int(input("Enter amount : "))
# t = int(input("Enter time period : "))
# r = int(input("Enter rate : "))
# interest = (p * t *r)/ 100
# interest2 = (p * t *r)// 100
# print("The interest is : " , interest)
# print("The interest is : " , interest2)

### Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

# For example:
# Input:
# heads -> 4
# legs -> 12
# <br>
# Output:
# dogs -> 2
# chicken -> 2

### Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.
# n = int(input("Enter a number : "))
# result = (n * (n + 1) * ((2 * n) + 1  ) )/ 6
# print("Result is " , result)

### Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.
# first_term = int(input("Enter first term : "))
# second_term = int(input("Enter second term : "))
# n = int(input("Enter nth term : "))
# d = second_term - first_term
# nth_term = first_term + (n - 1) * d
# print("The nth term is : " , nth_term)

### Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.
# n1 = int(input("Enter numerator of 1st fraction : "))
# d1 = int(input("Enter denominator of 1st fraction : "))
# n2 = int(input("Enter numerator of 2nd fraction : "))
# d2 = int(input("Enter denominator of 2nd fraction : "))
# result_n = n1 * d2 + n2 * d1
# result_d = d1 * d2
# print('{}/{}' . format(result_n , result_d)) # or
# print("The sum is : " , result_n , "/" , result_d)

### Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.

# Input:<br>
# Dimensions of the milk tank<br>
# H = 20cm, L = 20cm, B = 20cm
# <br><br>
# Dimensions of the glass<br>
# h = 3cm, r = 1cm

import math
h_t = int(input("Enter height of tank : "))
l_t = int(input("Enter length of tank : "))
b_t = int(input("Enter breadth of tank : "))

h_g = int(input("Enter height of glass : "))
r_g = int(input("Enter radius of glass : "))

volume_tank = h_t * l_t * b_t
volume_glass = 3.14*(r_g**2)*r_g*h_g
print("No of glasses : " , math.floor(volume_tank/volume_glass) )
