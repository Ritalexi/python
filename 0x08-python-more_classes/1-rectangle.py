#!/usr/bin/python3
""" Module that defines a rectangle"""


class Rectangle:
   """
   class Rectangle defines a rectangle
   """

    @property
    def width(self):
        """gets the width
        """
        
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width
        Args:
        value - width of the rectangle
        """
        
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """gets the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height
        Args:
        value - height of the rectangle
        """
        
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def __init__(self, width=0, height=0):
        """
        instantises the width and height
        """
        self.width = width
        self.height = height
