#!/usr/bin/env python
"""Write a function, f, which, given a list, removes consecutive duplicates
from it.

>>> f([1, 1, 2, 2, 2, 3, 4, 4])
[1, 2, 3, 4]
>>> f([1, 1, 2, 1])
[1, 2, 1]
>>> f([1, 1.0, 1])
[1, 1.0, 1]
>>> f([])
[]
>>> f(["A", "a", "B", "B", "c", "A", "A", "d", "d", "A"])
["A", "a", B", "c", "A", "d", "A"]
>>> f([4, 4, "a", "b", 2.0, 2.0, 2.0, [], []])
[4, "a", "b", 2.0, []]
"""

import doctest

# TODO: REPLACE ME WITH YOUR SOLUTION

if __name__ == "__main__":
    doctest.testmod()
