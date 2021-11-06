"""
Author: Mai Văn Hùng
Date: 24/10/2021
Program: Explain how an algorithm solves a general class of problems and how a function
definition can support this property of an algorithm.
Solution:
- An algorithm is a general method for solving a class of problems. The individual problems
that make up a class of problems are known as problem instances. The problem instances
for our summation algorithm are the pairs of numbers that specify the lower and upper
bounds of the range of numbers to be summed. The problem instances of a given algorithm
can vary from program to program, or even within different parts of the same program.
- The summation function contains both the code for the summation algorithm and the
means of supplying problem instances to this algorithm. The problem instances are the data
sent as arguments to the function. The parameters or argument names in the function’s
header behave like variables waiting to be assigned data whenever the function is called.
If designed properly, a function’s code captures an algorithm as a general method for solv-ing a class of problems. The function’s arguments provide the means for systematically
varying the problem instances that its algorithm solves. Additional arguments can broaden
the range of problems that are solvable. For example, the summation function could take a
third argument that specifies the step to take between numbers in the range. We will exam-ine shortly how to provide additional arguments that do not add complexity to a function’s
default uses.
    ....
"""