#!/usr/bin/python3
"""
module - 7-base_geometry.py
"""


class BaseGeometry:
    """
    A class that passes
    """

    def area(self):
        """
        Raise an Exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Args:
        name - string
        value - integer
        Raise Exceptions
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
