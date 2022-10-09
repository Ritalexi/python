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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """Return private attribute"""
        return self.width
    @width.setter
    def width(self, width):
        """Setting private attribute"""
        self.width = width

    @property
    def height(self):
        """Return private attribute"""
        return self.height
    @height.setter
    def height(self, height):
        """Setting private attribute"""
        self.height = height

    @property
    def x(self):
        """Return private attribute"""
        return self.x
    @x.setter
    def x(self, x):
        """Setting private attribute"""
        self.x = x

    @property
    def y(self):
        """Return private attribute"""
        return self.y
    @y.setter
    def y(self, y):
        """Setting private attribute"""
        self.y = y
