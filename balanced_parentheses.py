#!/usr/bin/env python
"""Write a function, f, which returns True/False to indicate whether the
parentheses in its input string are balanced.

>>> f("")  # empty string is balanced
True
>>> f("((()))")
True
>>> f("()()")
True
>>> f("](#((_)(_)))@( )(((foo))(bar))!{")  # other characters ignored
True
>>> f("((()")
False
>>> f("())")
False
>>> f(")(")  # order matters
False
>>> f("(()){}()(]")  # only () count, not [] or {}
False
"""

import doctest

# TODO: REPLACE ME WITH YOUR SOLUTION

if __name__ == "__main__":
    doctest.testmod()
