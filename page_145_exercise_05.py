"""
Author: Mai Văn Hùng
Date: 10/10/2021
Program: Assume that data refers to a list of numbers, and result refers to an empty list.
Write a loop that adds the nonzero values in data to the result list, keeping them
in their relative positions and excluding the zeros.
Solution:
    ....
"""
data = [75,50,88,64,100]
result = ""
for number in data:
   if number != 0:
       result += str(number)

