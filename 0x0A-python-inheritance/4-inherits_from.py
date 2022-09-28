#!/usr/bin/python3
"""
A function that returns True
if the object is an instance of a class that inherited
from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """
    Args:
    obj - object
    a_class - class
    Returns:
    True  - if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class 
    otherwise False
    """

    if type(obj) != a_class:
        return True
    return False
