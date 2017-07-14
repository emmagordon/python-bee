#!/usr/bin/env python
"""Write a function, f, which, given a positive integer, returns the
value as a roman numeral.

where, in roman numerals:
i = 1
v = 5
x = 10
l = 50
c = 100
d = 500

The value you return should use as few characters as possible, e.g. 4
should be 'iv' rather than 'iiii'.

You can assume the number you have to convert is < 1000.

>>> f(1) in ['i', 'I']
True
>>> f(4) in ['iv', 'IV']
True
>>> f(36) in ['xxxvi', 'XXXVI']
True
>>> f(140) in ['cxl', 'CXL']
True
>>> f(827) in ['dcccxxvii', 'DCCCXXVII']
True
"""

import doctest

# TODO: REPLACE ME WITH YOUR SOLUTION

if __name__ == "__main__":
    doctest.testmod()
