"""
Author: Mai Van Hung
Date: 4/9/2021
Problem:
    The tax calculator program of the case study outputs a floating-point number
    that might show more than two digits of precision. Use the round function to
    modify the program to display at most two digits of precision in the output
    number.
Solution:

"""
# Initialize the constants
TAX_RATE = 0.20
STANDARD_DETRUCTION = 10000.0
DEPENDENT_DETRUCTION = 3000.0

# Request the input
grossIncome = float(input("Enter the gross income: "))
numdependents = int(input("Enter the number of dependents: "))

# Comepute the income tax
Taxableincome = grossIncome - STANDARD_DETRUCTION - \
                DEPENDENT_DETRUCTION + numdependents
incometax = Taxableincome * TAX_RATE

# Display the income tax
print("the income tax is $" + str(round(incometax, 2)))
