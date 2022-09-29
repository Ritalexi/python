#!/usr/bin/python3
"""module: 4-inherits_from
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

    return type(obj) != a_class and isinstance(obj, a_class)
