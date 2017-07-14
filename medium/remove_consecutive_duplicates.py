#!/usr/bin/env python
"""Write a function, f, which, given a list, returns a copy of the list
with consecutive duplicates removed from it.

The list may contain integers, floats, strings, booleans and/or None.
You should consider 1 and 1.0 (for example) as distinct values.

>>> f([1, 1, 2, 2, 2, 3, 4, 4])
[1, 2, 3, 4]
>>> f([1, 1, 2, 1])
[1, 2, 1]
>>> f([1, 1.0, 1])
[1, 1.0, 1]
>>> f([])
[]
>>> f(['A', 'a', 'B', 'B', 'c', 'A', 'A', 'd', 'd', 'A'])
['A', 'a', 'B', 'c', 'A', 'd', 'A']
>>> f([4, 4, 'a', 'b', 2.0, 2.0, 2.0, 2, 2])
[4, 'a', 'b', 2.0, 2]
>>> f([False, False, 0, True, True, 1])
[False, 0, True, 1]
>>> f([None, None, 1, None])
[None, 1, None]
"""

import doctest

# TODO: REPLACE ME WITH YOUR SOLUTION

if __name__ == "__main__":
    doctest.testmod()
