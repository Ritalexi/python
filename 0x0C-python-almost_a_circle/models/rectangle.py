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
        return self.__width
    @width.setter
    def width(self, value):
        """Setting private attribute"""
        self.validation("width", value)
        self.__width = value

    @property
    def height(self):
        """Return private attribute"""
        return self.__height
    @height.setter
    def height(self, value):
        """Setting private attribute"""
        self.validation("height", value)
        self.__height = value

    @property
    def x(self):
        """Return private attribute"""
        return self.__x
    @x.setter
    def x(self, value):
        """Setting private attribute"""
        self.validation("x", value)
        self.__x = value

    @property
    def y(self):
        """Return private attribute"""
        return self.__y
    @y.setter
    def y(self, value):
        """Setting private attribute"""
        self.validation("y", value)
        self.__y = value

    @staticmethod
    def validation(attribute, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def area(self):
        """
        returns the area value of the Rectangle instance
        """
        return (self.__width * self.__height)

    def display(self):
        """
        prints in stdout the Rectangle
        instance with the character #
        """
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        update the class Rectangle
        and return a string
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.__x,
                                                        self.__y,
                                                        self.__width,
                                                        self.__height))
