#!/usr/bin/python3
"""
Module of the rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """
    Defining class Rectangle
    initialization from:
    base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        Base.__init__(self, id)

    @property
    def width(self):
        """Return private attribute"""
        return self.__width
    @width.setter
    def width(self, width):
        """Setting private attribute"""
        self.___width = width

    @property
    def height(self):
        """Return private attribute"""
        return self.__height
    @height.setter
    def height(self, height):
        """Setting private attribute"""
        self.__height = height

    @property
    def x(self):
        """Return private attribute"""
        return self.__x
    @x.setter
    def x(self, x):
        """Setting private attribute"""
        self.__x = x

    @property
    def y(self):
        """Return private attribute"""
        return self.__y
    @y.setter
    def y(self, y):
        """Setting private attribute"""
        self.__y = y
