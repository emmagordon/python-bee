#!/usr/bin/env python
"""Write a function, f, which takes two positive integers as input and
returns a string containing the digits of the first number in the base
of the second number.

If the base is larger than 10, you should use the alphabet for digits
beyond 9, e.g. 'a' for 10. You may assume you won't need anything
larger than 'z'!

>>> f(123758, 10)
'123758'
>>> f(0, 7)
'0'
>>> f(9, 2)
'1001'
>>> f(34, 3)
'1021'
>>> f(15, 8)
'17'
>>> f(28, 16) in ['1c', '1C']
True
>>> f(19, 20) in ['j', 'J']
True
"""

import doctest

# TODO: REPLACE ME WITH YOUR SOLUTION

if __name__ == "__main__":
    doctest.testmod()
