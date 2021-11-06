"""
Author: Mai Văn Hùng
Date: 24/10/2021
Program:What is the scope of a variable? Give an example.
Solution:
In ordinary writing, the meaning of a word often depends on its surrounding context. For
example, in the sports section of the newspaper, the word “bat” means a stick for hitting
baseballs, whereas in a story about vampires it means a flying mammal. In a program, the
context that gives a name a meaning is called its scope. In Python, a name’s scope is the
area of program text in which the name refers to a given value
Example:
    x = 5
def f():
 x = 10 # Attempt to reset x
f() # Does the top-level x change?
print(x) # No, this displays 5
    ....
"""