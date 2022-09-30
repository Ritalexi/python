#!/usr/bin/python3
"""
Module 8-rectangle.py
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Implements a rectangle
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        BaseGeometry.integer_validator(self, width, height)
