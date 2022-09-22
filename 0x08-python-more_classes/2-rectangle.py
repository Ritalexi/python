#!/usr/bin/python3
""" Method that defines a rectangle"""


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
        """
        self.width = width
        self.height = height

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

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if ((self.__width == 0) or (self.__height == 0)):
            return (0)
        return (2 * (self.__width + self.__height))
