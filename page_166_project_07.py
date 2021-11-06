"""
Author: Mai Văn Hùng
Date: 10/10/2021
Program: Write a program that inputs a text file. The program should print the unique
words in the file in alphabetical order.
Solution:
    ....
"""
file_input = input("Import file here: ")
with open (file_input,'r') as f:
    fp=f.read().split()
fp=set(fp)
fp=sorted(fp)
print(fp)
print("Number of unique words: {0}".format(len(fp)))
