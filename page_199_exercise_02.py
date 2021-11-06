"""
Author: Mai Văn Hùng
Date: 24/10/2021
Program:Write the code for a filtering that generates a list of the positive numbers in a list
named numbers. You should use a lambda to create the auxiliary function
Solution:

    ....
"""
numbers = [15, 7, 8, -21, 13, -69, 96, 55,78]
print("Số ban đầu trong danh sách: ",numbers)
print("Các số dương trong danh sách đã nói: ")
for pos_nums in numbers:
   if pos_nums > 0:
      print(pos_nums, end = " ")