#!/usr/bin/env python
"""Example for explaining the rules, this problem does not
count for points!

Write a function, f, which takes arbitary input yet always
returns "Hello World".

>>> f()
"Hello World"
>>> f(1)
"Hello World"
>>> f("test", test="this")
"Hello World"
"""

import doctest


def f(*a, **k):
    return "Hello World"

if __name__ == "__main__":
    doctest.testmod()
