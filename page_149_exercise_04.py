"""
Author: Mai Văn Hùng
Date: 10/10/2021
Program: Define a function named summation. This function expects two numbers, named
low and high, as arguments. The function computes and returns the sum of the
numbers between low and high, inclusive.
Solution:
    ....
"""
lower = int(input("Nhập giới hạn dưới: "))
upper = int(input("Nhập giới hạn trên: "))
the_sum = 0
for number in range(lower, upper + 1):
    the_sum = the_sum + number
    print(the_sum)

