"""
Author: Mai Văn Hùng
Date: 24/10/2021
Program: Write the code for a mapping that generates a list of the absolute values of the numbers in a list named numbers.
Solution:

    ....
"""
number = [1, -2, 3, -4, -5]
print("The original list is : " + str(number))
res = list(map(abs, number))
print("Absolute value list : " + str(res))