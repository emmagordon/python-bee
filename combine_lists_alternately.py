#!/usr/bin/env python
"""Write a function, f, which combines two lists by taking alternate
elements from them. If the lists are different lengths, throw away
the extra elements.

>>> f([1,2], [3, 4])
[1, 3, 2, 4]
>>> f([], [])
[]
>>> f([1, 2, 3], [4])
[1, 4]
>>> f([1], [2, 3])
[1, 2]
>>> f([1, 2, 3], [])
[]
>>> f([1.0, 'mixed'], [{1: 2}, (3,)])
[1.0, {1: 2}, 'mixed', (3,)]
>>> f([1, 2, 3, 4, 5], ['one', 'two', 'three', 'four', 'five'])
[1, 'one', 2, 'two', 3, 'three', 4, 'four', 5, 'five']
"""

import doctest

# TODO: REPLACE ME WITH YOUR SOLUTION

if __name__ == "__main__":
    doctest.testmod()
