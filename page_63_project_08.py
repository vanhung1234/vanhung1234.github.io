"""
Author: Mai Van Hung
Date: 4/9/2021
Problem:
    Light travels at 3 *108
    meters per second. A light-year is the distance a light beam
    travels in one year. Write a program that calculates and displays the value of a light-year
Solution:

"""
# Compute the results
rate = 3 * 10 ** 8
seconds = 365 * 24 * 60 ** 2
distance = rate * seconds

# Display the results
print("Light travels", distance , " Enter in a year.")
