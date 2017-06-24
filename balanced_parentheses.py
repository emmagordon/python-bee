#!/usr/bin/env python
"""Write a function, f, which returns True/False to indicate whether the
parentheses in its input string are balanced.

>>> f("")
True
>>> f("((()))")
True
>>> f("()()")
True
>>> f("[(#((_)(_)))@( )(((foo))(bar))!}")
True
>>> f("((()")
False
>>> f("())")
False
>>> f("(()){}()(]")
False
"""

import doctest

# REPLACE WITH ME WITH YOUR SOLUTION

if __name__ == "__main__":
    doctest.testmod()
