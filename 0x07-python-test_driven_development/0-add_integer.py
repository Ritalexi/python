#!/usr/bin/python3
"""Write a function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Add two integers
    Args:
        a - integer or float
        b - integer or float
    raise: a and b must be integers or floats
           else raise type error exception
    """
    if (isinstance(a, float) or isinstance(b, float)):
        a = int(a)
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    
    return a + b
