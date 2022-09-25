#!/usr/bin/python3
"""
Module that defines a rectangle
"""


class Rectangle:
    """
        Rectangle defines a rectangle
        Attributes:
            width: width of rectangle
            height: height of rectangle
        Method:
            __init__: Initializes width and height for all instances
    """

    number_of_instances = 0
    print_symbol = "#"


    def __init__(self, width=0, height=0):
        """
        initialization of the width and height
        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

        type(self).number_of_instances += 1

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

    def area(self):
        """
        function that returns the rectangle area
        """
        return (self.width * self.height)

    def perimeter(self):
        """
        function that returns the perimemter area
        """
        if ((self.width == 0) or (self.height == 0)):
            return (0)
        return (2 * (self.width + self.height))

    def __str__(self):
        """
        Prints the rectangle with the character #
        """
        if ((self.width == 0) or (self.height == 0)):
            return ("")
        rect = []
        for i in range(self.height):
            for j in range(self.width):
                rect.append(str(self.print_symbol))
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        to be able to recreate a new instance
        """
        rect = "Rectangle(" + str(self.width)
        rect += ", " + str(self.height) + ")"
        return (rect)

    def __del__(self):
        """
        A function Print the message Bye rectangle...
        """
        print ("Bye rectangle...")
        type(self).number_of_instances -= 1
