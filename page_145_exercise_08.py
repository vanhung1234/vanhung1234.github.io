"""
Author: Mai Văn Hùng
Date: 10/10/2021
Program: Explain the difference between structural equivalence and object identity.
Solution:
    Occasionally, programmers need to see whether two variables refer to the exact same object or
to different objects. For example, you might want to determine whether one variable is an alias
for another. The == operator returns True if the variables are aliases for the same object.
Unfor-tunately, == also returns True if the contents of two different objects are the same.
The first rela-tion is called object identity, whereas the second relation is called structural equivalence.
The == operator has no way of distinguishing between these two types of relations
    ....
"""

