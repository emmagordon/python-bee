#!/usr/bin/env python
"""Write a function, f, which takes arbitrary input and returns
True/False for even/odd numbers of input arguments respectively.

>>> f()
True
>>> f(True)
False
>>> f("test", test="this")
True
>>>f([1, 2])
False
>>> f(1, [1, 2], {}, "baz", 2.0, False, foo="bar", baz="FOO")
True
"""

import doctest

# TODO: REPLACE ME WITH YOUR SOLUTION

if __name__ == "__main__":
    doctest.testmod()
