#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle:
    """
        Rectangle defines a rectangle
        Attributes:
            width: width of rectangle
            height: height of rectangle
        Method:
            __init__: Initializes width and height for all instances
    """

    def __init__(self, width=0, height=0):
        """
        initialization of the width and height
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter function for the width
           Returns: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter function for the width
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
        """getter function for the height
           Returns: the height of the rectangle
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
