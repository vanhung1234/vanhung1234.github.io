"""
Author: Mai Văn Hùng
Date: 24/10/2021
Program: What is the lifetime of a variable? Give an example.
Solution:
A computer program has two natures. On the one hand, a program is a piece of text con-taining names that a human being can read for a meaning. Viewed from this perspective,
variables in a program have a scope that determines their visibility. On the other hand, a
program describes a process that exists for a period of time on a real computer. Viewed
from this other perspective, a program’s variables have another important property called a
lifetime. A variable’s lifetime is the period of time during program execution when the vari-able has memory storage associated with it. When a variable comes into existence, storage
is allocated for it; when it goes out of existence, storage is reclaimed by the PVM
Example:
The concept of lifetime explains the existence of two variables called x in our last
example session. The module variable x comes into existence before the temporaryvariable x and survives the call of function f. During the call of f, storage exists for both
variables, so their values remain distinct. A similar mechanism for managing the stor-age associated with the parameters of recursive function calls was discussed in the pre-vious section
    ....
"""