"""
Author: Mai Văn Hùng
Date: 10/10/2021
Program:
  Write a program that allows the user to navigate the lines of text in a file. The
program should prompt the user for a filename and input the lines of text into a
list. The program then enters a loop in which it prints the number of lines in the
file and prompts the user for a line number. Actual line numbers range from 1 to
the number of lines in the file. If the input is 0, the program quits. Otherwise, the
program prints the line associated with that number.

Solution:

    ....
"""

enterfile = input("Import file name: ")
file = open(enterfile, 'r')
linecount = 0
for line in file:
    linecount = linecount + 1
print("Number of lines in this txt. file is ", linecount)
while True:
    linenum = 0
    num = int(input("Please enter line number or press 0 to exit: "))
    if num >=1 and num <= linecount:
        file = open(enterfile, 'r')
        for lines in file:
            linenum = linenum + 1
            if linenum == num:
                print(lines)
    else:
        if num == 0:
            print("Thank you for using the program")
            break

