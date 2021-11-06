"""
Author: Mai Van Hung
Date: 4/9/2021
Problem:

Solution:

"""

import math

# Request the input
Radius = float(input("Enter the sphere's radius: "))

# Compute the results
diameter = 2 * Radius
cicumference = diameter * math.pi
surfaceArea = 4 * math.pi * Radius * Radius
volume = 4 / 3.0 * math.pi * Radius * Radius * Radius

# Dis[lay the results
print("Diameter     :", diameter)
print("Cicumference :", cicumference)
print("Surface area :", surfaceArea)
print("Volume       :", volume)