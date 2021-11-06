"""
Author: Mai Văn Hùng
Date: 10/10/2021
Program: What is the purpose of a main function?
Solution:
    The main function prompts the user for a number, calls the square function to compute its square, and prints the result.
You can define the main and the square functions in any order. When Python loads this module,
the code for both function definitions is loaded and compiled, but not executed. Note that
main is then called within an if statement as the last step in the script. This has the effect of
transferring control to the first instruction in the main function’s definition. When square is
called from main, control is transferred from main to the first instruction in square. When a
function completes execution, control returns to the next instruction in the caller’s code.
    ....
"""

