#!/usr/bin/env python
"""Write a function, f, which takes a positive integer as input and
returns True if it is 'perfect', or False otherwise.

A number is 'perfect' if the sum if its divisors (exclusing the number
itself) equal the number itself.

The smallest perfect number is 6. This has divisors 1, 2 and 3, where
1 + 2 + 3 = 6.

>>> f(1)
False
>>> f(6)
True
>>> f(7)
False
>>> f(496)
True
>>> f(500)
False
>>> f(8128)
True
"""

import doctest

# TODO: REPLACE ME WITH YOUR SOLUTION

if __name__ == "__main__":
    doctest.testmod()
