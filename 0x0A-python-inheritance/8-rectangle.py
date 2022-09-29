#!/usr/bin/python3
"""
Module 8-rectangle.py
"""


class Rectangle(BaseGeometry):
    """
    Implements a rectangle
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.integer_validator(self, width, height)
