#!/usr/bin/env python
"""Write a function, f, which takes in a number and returns
"fizz"/"buzz" if it's a multiple of 3/5 respectively, "fizzbuzz"
 if it's a multiple of both, and None otherwise.

>>> f(9)
"fizz"
>>> f(10.0)
"buzz"
>>> f(45)
"fizzbuzz"
>>> f(-3)
"fizz"
>>> f(2)
None
>>> f(15.0000000001)
None
"""

import doctest


def f(n):
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return 'fizz'
    if n % 5 == 0:
        return 'buzz'


if __name__ == "__main__":
    doctest.testmod()