"""
Author: Mai Van Hung
Date: 4/9/2021
Problem:
    Explain how to display help information on a particular function in a given module
Solution:
    After importing a main module, you can view its documentation by running the help function:
    >>> help(taxform)
    DESCRIPTION
    Program: taxform.py
    Author: Ken
    Compute a person’s income tax.
    Significant constants
    tax rate
    standard deduction
    deduction per dependent
    The inputs are
    gross income
    number of dependents
    Computations:
    net income 5 gross income - the standard deduction - a
    deduction for each dependent
    income tax 5 is a fixed percentage of the net income
    The outputs are
    the income tax
    ....
"""