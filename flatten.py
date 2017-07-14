#!/usr/bin/env python
"""Write a function, f, which takes an input list and flattens it.

You may not use the itertools module.

>>> f([[[]]])
[]
>>> f([[[1]]])
[1]
>>> f([['a'], ['b', 'c']])
['a', 'b', 'c']
>>> f([[1, 2], 3, [4, [5, 6]]])
[1, 2, 3, 4, 5, 6]
>>> f(['already', 'f[la]t'])
['already', 'f[la]t']
>>> f([1, [2], 3])
[1, 2, 3]
"""

import doctest

# TODO: REPLACE ME WITH YOUR SOLUTION

if __name__ == "__main__":
    doctest.testmod()
