"""
Author: Mai Văn Hùng
Date: 10/10/2021
Program: Write a loop that replaces each number in a list named data with its absolute value.
Solution:
    ....
"""
data=[-5,-4,-3,11,7,4]
processed = []
for number in data:
    if number < 0:
        processed.append(abs(number))
    else:
        processed.append(number)
print("Original numbers:\n", data)
print("Processed numbers:\n", processed)
