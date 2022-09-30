#!/usr/bin/python3
"""Contains a class that inherits from `BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ instantiation with size """
        self.__size = size
        self.integer_validator(size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        """ print """
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
