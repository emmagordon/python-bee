#!/usr/bin/env python
"""Write a function, f, which returns True/False to indicate whether the
parentheses in its input string are balanced.

>>> f("")
True
>>> f("((()))")
True
>>> f("()()")
True
>>> f("](#((_)(_)))@( )(((foo))(bar))!{")
True
>>> f("((()")
False
>>> f("())")
False
>>> f(")(")
False
>>> f("(()){}()(]")
False
"""

import doctest

# TODO: REPLACE ME WITH YOUR SOLUTION

def f(s):
    count = 0
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0
            return false
    return count == 0


if __name__ == "__main__":
    doctest.testmod()
